from django.shortcuts import render, get_object_or_404
from websitetext.models import Training

# Create your views here.
def training(request):
    text = get_object_or_404(Training)
    template = 'training/training.html'
    context = {'text': text}
    return render(request, template, context)

def beginners(request):
    text = get_object_or_404(Training)
    template = 'training/beginners.html'
    context = {'text': text}
    return render(request, template, context)

def calendar(request):
    text = get_object_or_404(Training)
    template = 'training/calendar.html'
    context = {'text': text}
    return render(request, template, context)