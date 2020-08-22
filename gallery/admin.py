from django.contrib import admin

# Register your models here.
from .models import NewAlbum, NewAlbumPhoto


admin.site.register(NewAlbum)
admin.site.register(NewAlbumPhoto)