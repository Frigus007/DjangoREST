from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
app_name="blog"
urlpatterns=[
    #url(r'^$',views.home,name='home'),
    #url(r'^add_blog/$',views.create_blog,name='add'),
    #url(r'^list/$',views.display,name='list'),
    #url(r'^detailed/(?P<pk>\d+)/', views.detail, name='detail'),

    #url(r'^contact/',views.contact,name='contact'),
    #path("register/", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)