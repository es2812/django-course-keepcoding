from django.urls import path, include
from photos.api import PhotoViewSet
from rest_framework.routers import DefaultRouter

# APIRouter
router = DefaultRouter()
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('1.0/', include(router.urls))
]