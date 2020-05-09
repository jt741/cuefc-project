from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def allnews(request):
    posts = BlogPost.objects
    return render(request, 'teamnews/allnews.html', {'posts': posts})

