from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from teamnews.models import BlogPost
from django.core.mail import EmailMessage, send_mail
from websitetext.models import Training

import operator

def home(request): #request object
    posts = BlogPost.objects.order_by('-pub_date')[:3]
    
    return render(request, 'home.html', {'posts': posts})



def pandf(request):
    text = get_object_or_404(Training)
    template = 'practicesandfixtures.html'
    context = {'text' : text}
    return render(request, template, context)
    

def contactus(request):
    Contact_Form = ContactForm
    ss = False 
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            
            content ={
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content
            }

            content = template.render(content)

            send_mail(
                'CUEFC website message',
                content,
                'jexi.griffins@gmail.com',
                ['denoxeh463@qortu.com'],
                fail_silently=False
            )

            ss = True

    return render(request, 'contact.html', {'successful_submit': ss})

def donate(request):
    template = 'donate.html'
    return render(request, template)

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm



from django.template import Template
from django.template.loader import get_template
import os
from django.conf import settings


##this is the test one!
'''
def contact(request):
    directory = r'cuefc\static'
    piclist = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            piclist.append(filename)
        else:
            continue
    


    return render(request, 'contactemail.html', {'piclist': piclist})
'''

from websitetext.models import AboutFives


def contact(request):
    text = get_object_or_404(AboutFives)
    template = 'contactemail.html' 
    context = {'text' : text}
    return render(request, template, context)


