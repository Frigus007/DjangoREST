from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
app_name="blog"
urlpatterns=[

    path('', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)