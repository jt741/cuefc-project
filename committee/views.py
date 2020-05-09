from django.shortcuts import render, get_object_or_404

from .models import Member
# Create your views here.

def committee(request):
    members = Member.objects
    return render(request, 'committee/committee.html', {'members': members})
