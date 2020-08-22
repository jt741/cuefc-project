from django.shortcuts import render, get_object_or_404
from .models import NewAlbum, NewAlbumPhoto
# Create your views here.

def gallery(request):
    albums = NewAlbum.objects.all()
    photos = NewAlbumPhoto.objects.all()
    return render(request, 'gallery/gallery.html', {"albums": albums, "photos": photos})

