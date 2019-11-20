from django.shortcuts import render
from django.http.response import HttpResponse
from photos.models import Photo

def home(request):
    photos = Photo.objects.all()
    
    return render(request, "photos/home.html", context={"photo_list": photos})