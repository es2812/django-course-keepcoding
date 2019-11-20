from django.shortcuts import render
from django.http.response import HttpResponse
from photos.models import Photo

def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    context = {
        "photo_list": photos[0:5]
    }
    return render(request, "photos/home.html", context)