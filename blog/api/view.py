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


