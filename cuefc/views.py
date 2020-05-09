from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request): #request object
    return render(request, 'home.html')

def ctest(request):
    return render(request, 'ctest.html')

def pandf(request):
    return render(request, 'practicesandfixtures.html')