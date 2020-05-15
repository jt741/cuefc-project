from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def allnews(request):
    posts = BlogPost.objects
    return render(request, 'teamnews/about.html', {'posts': posts})

def teamnews(request):
    posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'teamnews/teamnews.html', {'posts': posts})

def committee(request):
    return render(request, 'committee/committee.html') #idk why but it auto goes to committee even if u type teamnews!

def sponsership(request):
    return render(request, 'teamnews/sponsership.html')

def newsdetail(request, newspost_id):
    detailnewspost = get_object_or_404(BlogPost, pk=newspost_id)
    return render(request, 'teamnews/newsdetail.html', {'newspost': detailnewspost})