
from teamnews.models import BlogPost

from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.template.loader import get_template


def home(request):
    posts = BlogPost.objects.order_by('-pub_date')[:3]
    
    return render(request, 'home.html', {'posts': posts})


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







