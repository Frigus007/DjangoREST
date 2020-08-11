from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog" ,null=True)
    uploaded_by=models.CharField(max_length=100,default='')
    discription=models.CharField(max_length=20000,default='')
    user_discription=models.CharField(max_length=200,default='')
    location_city=models.CharField(max_length=100,default='')
    location_state=models.CharField(max_length=100,default='')
    Country=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to='blog_img/',blank=True,max_length=255)
    title=models.CharField(max_length=50,default='')
    #picture=models.FileField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.discription

    @property
    def comments(self):
        return self.comments_set.all()
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100,default='')
    comment=models.CharField(max_length=200,default='')
    time=models.DateTimeField(auto_now=True)

class Hotels(models.Model):
    uploaded_by=models.CharField(max_length=100,default='')
    discription=models.CharField(max_length=2000,default='')
    location_city=models.CharField(max_length=100,default='')
    location_state=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to='hotel_img',blank=True)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.uploaded_by