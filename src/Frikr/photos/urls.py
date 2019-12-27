from django.urls import path, include
from django.contrib.auth.decorators import login_required
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView

urlpatterns = [
    # Photos URLs
    path('', HomeView.as_view(), name="photos_home"),
    path('photos', PhotoListView.as_view(), name="photos_list"),
    path('photos/<int:pk>/', DetailView.as_view(), name="photos_detail"),
    path('photos/create', CreateView.as_view(), name="create_photo"),
    path('my-photos', login_required(UserPhotosView.as_view()), name="user_photos"),
]