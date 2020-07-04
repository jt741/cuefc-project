from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from websitetext.models import AboutFives
from django.db.models import Q

# Create your views here.
def allnews(request):
    text = get_object_or_404(AboutFives)
    template = 'teamnews/about.html'
    context = {'text' : text}
    return render(request, template, context)
    

def teamnews(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
        print('nothing was searched')
            
    if q:
        posts = BlogPost.objects.filter(Q(title__icontains=q) | Q(body__icontains=q)).order_by('-pub_date')
        print(posts)
        context = {'query' : q, 'posts': posts}

    else:
        posts = BlogPost.objects.order_by('-pub_date')
        context = {'posts': posts}

    return render(request, 'teamnews/teamnews.html', context)

def committee(request):
    return render(request, 'committee/committee.html') #idk why but it auto goes to committee even if u type teamnews!

def sponsership(request):
    return render(request, 'teamnews/sponsership.html')

def newsdetail(request, newspost_id):
    detailnewspost = get_object_or_404(BlogPost, pk=newspost_id)
    return render(request, 'teamnews/newsdetail.html', {'newspost': detailnewspost})

def captains(request):
    return render(request, 'teamnews/captains.html')