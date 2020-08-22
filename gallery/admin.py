from django.contrib import admin

# Register your models here.
from .models import Album, NewAlbum, NewAlbumPhoto

admin.site.register(Album)
admin.site.register(NewAlbum)
admin.site.register(NewAlbumPhoto)