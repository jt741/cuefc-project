from django.http import HttpResponse
from django.shortcuts import render
from teamnews.models import BlogPost

import operator

def home(request): #request object
    posts = BlogPost.objects.order_by('-pub_date')[:3]
    return render(request, 'home.html', {'posts': posts})

def ctest(request):
    return render(request, 'ctest.html')

def pandf(request):
    return render(request, 'practicesandfixtures.html')

def contactus(request):
    return render(request, 'contact.html')