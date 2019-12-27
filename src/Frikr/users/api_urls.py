from django.urls import path, include
from users.api import UserViewSet
from rest_framework.routers import DefaultRouter

# APIRouter
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('1.0/', include(router.urls))
]