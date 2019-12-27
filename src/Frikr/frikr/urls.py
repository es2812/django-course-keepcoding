from django.contrib import admin
from django.urls import path, include

import photos.urls as photos_urls
import users.urls as users_urls

import photos.api_urls as api_photos_urls
import users.api_urls as api_users_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(photos_urls)),
    path('', include(users_urls)),
    
    path('api/', include(api_photos_urls)),
    path('api/', include(api_users_urls))
]