from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

@login_required()
def create(request):
    success_msg = ""
    if request.method == "GET":
        form = PhotoForm()
    else:
        owned_photo = Photo()
        owned_photo.owner = request.user #asign authenticated user as owner    
        form = PhotoForm(request.POST, instance=owned_photo)
        if form.is_valid():
            new_photo = form.save() # Saves Photo object and returns it
            form = PhotoForm()
            success_msg = "Foto guardada con éxito."
            success_msg += "<a href='{0}'>".format(reverse('photos_detail', args=[new_photo.pk]))
            success_msg += "Ver foto"
            success_msg += "</a>."

    context = {
        'form': form,
        'msg' : success_msg
    }

    return render(request, "photos/new_photo.html", context)