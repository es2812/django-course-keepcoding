"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from photos import views as photo_views
from photos.views import HomeView, DetailView
from users.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Photos URLs
    path('', HomeView.as_view(), name="photos_home"),
    path('photos/<int:photo_id>/', DetailView.as_view(), name="photos_detail"),
    path('photos/create', photo_views.create, name="create_photo"),

    # Users URLs
    path('login', LoginView.as_view(), name="users_login"),
    path('logout', LogoutView.as_view(), name="users_logout")
]