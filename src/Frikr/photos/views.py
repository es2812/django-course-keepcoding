from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC

def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        "photo_list": photos[0:5]
    }
    return render(request, "photos/home.html", context)


def detail(request, photo_id):
    pos_photos = Photo.objects.filter(pk=photo_id)
    photo = pos_photos[0] if len(pos_photos) == 1 else None

    if photo is not None:
        context = {
        "photo": photo
        }
        return render(request, "photos/detail.html", context)
    else:
        return HttpResponseNotFound() # 404 not found
