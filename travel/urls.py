
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^',include('blog.urls',namespace='blog')),
    path('admin/', admin.site.urls),
    #Rest api
    url(r'api/',include('blog.api.urls',namespace='blogapi')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)