from django.urls import path, include
from django.contrib.auth.decorators import login_required

from users.views import LoginView, LogoutView

urlpatterns = [
    # Users URLs
    path('login', LoginView.as_view(), name="users_login"),
    path('logout', LogoutView.as_view(), name="users_logout")
]