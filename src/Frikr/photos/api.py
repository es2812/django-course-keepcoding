from rest_framework.views import APIView
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotosQueryset
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

class PhotoViewSet(PhotosQueryset, ModelViewSet):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        # called before serializer.save()
        # automatically assigns ownership of photo to authenticated user
        serializer.save(owner=self.request.user)