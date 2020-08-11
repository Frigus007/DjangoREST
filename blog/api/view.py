from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from blog.models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from blog.api.serializers import *
from  rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET',])
def api_display_all(request):
    try:
        blog=Blog.objects.all()
        #print(blog)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=BlogViewSerializer(blog,many=True)
        return Response(serializer.data)

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def api_detail(request,pk):
        try:
            blog = Blog.objects.get(pk=pk)
            come = Comments.objects.all().filter(blog_id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if(request.method=='GET'):
            serializer=BlogSerializer(blog)
            serializer2=CommentSerilizer(come)
            return Response(serializer.data)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def api_createblog(request):
    user_id = Token.objects.get(key=request.auth.key).user_id
    print(user_id)
    new=request.data
    new['user_id']=user_id
    if request.method=='POST':
        serializer=BlogAddSerializer(data=new)
        data={}
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def api_reg(request):
    #user_reg=User()
    if request.method=="POST":
        serializer=Regserilizer(data=request.data)
        data={}
        if(serializer.is_valid()):
            user=serializer.save()
            data['response']='Successfully Reg'
        else:
            data=serializer.errors
        return Response(data)
@api_view(['PATCH',])
@permission_classes([IsAuthenticated])
def api_patch_blog(request):
    if request.method=="PATCH":
        try:
            #temp=request.data[id]
            print((request.data['id']))
            blog=Blog.objects.get(id=request.data['id'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializers=BlogViewSerializer(blog,data=request.data,partial=True)
        if serializers.is_valid():

            t=serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def api_delete_blog(request):
    if request.method=='DELETE':
        try:
            blog=Blog.objects.get(id=request.data['id'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response("Blog deleted", status=status.HTTP_204_NO_CONTENT)

