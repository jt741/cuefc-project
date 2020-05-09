from django.shortcuts import render
from .models import Album
# Create your views here.

def gallery(request):
    albums = Album.objects
    return render(request, 'gallery/gallery.html', {'albums': albums})