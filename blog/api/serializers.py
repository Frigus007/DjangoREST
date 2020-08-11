from rest_framework import serializers
#from django.contrib.auth.models import User
from blog.models import *
from  django.contrib.auth.models import User
class Regserilizer(serializers.ModelSerializer):
    password1=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields = ["username", "email", "password", "password1"]
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        user=User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        password1=self.validated_data['password1']
        if(password!=password1):
            raise serializers.ValidationError({'password':'must match'})
        user.set_password(password)
        user.save()
        return user


class CommentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=['name','comment','time']
class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerilizer(many=True)
    class Meta:
        model=Blog
        fields=['uploaded_by','discription','user_discription','location_city','location_state','Country','image','title','created_at','comments']

class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['uploaded_by','discription','user_discription','location_city','location_state','Country','image','title','created_at']
class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model=User
    fields = ('id','username','email')
    read_only_fields = ('created','updated')

class BlogAddSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model=Blog
        #fields=['user','uploaded_by','discription','user_discription','location_city','location_state','Country','image','title','created_at']
        fields = '__all__'