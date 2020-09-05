from django.contrib import admin

# Register your models here.
from .models import BlogPost, Document

admin.site.register(BlogPost)
admin.site.register(Document)