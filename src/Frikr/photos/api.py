from rest_framework.views import APIView
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer