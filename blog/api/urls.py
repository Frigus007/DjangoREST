from django.urls import path
from django.conf.urls import url
from blog.api.view import *
from rest_framework.authtoken import views
from django.conf.urls.static import static

from django.conf import settings


app_name='blog'
urlpatterns=[
    url(r'^$',api_display_all,name='home'),
    url(r'^detailed/(?P<pk>\d+)',api_detail, name='detailed'),
    url(r'^add_blog$',api_createblog,name='add'),
    url(r'^api-token-auth$',views.obtain_auth_token,name='api-auth-token'),
    url(r"^api_register", api_reg, name="reg"),
    url(r'^patch', api_patch_blog, name='patch'),
    url(r'^delete', api_delete_blog, name='delete'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)