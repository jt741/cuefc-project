
from teamnews.models import BlogPost
from websitetext.models import SupportTheClub, Donors
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm

from django.template.loader import get_template


def home(request):
    posts = BlogPost.objects.order_by('-pub_date')[:3]
    
    return render(request, 'home.html', {'posts': posts})


def contactus(request):
    Contact_Form = ContactForm
    NewsLetterLink = get_object_or_404(Donors)
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
                'cuetonfives@gmail.com',
                ['cuetonfives@gmail.com'],
                fail_silently=False
            )

            ss = True

    return render(request, 'contact.html', {'successful_submit': ss, "NewsLetterLink": NewsLetterLink})

def donate(request):
    text = get_object_or_404(SupportTheClub)
    template = 'donate.html'
    context = {'text': text}
    return render(request, template, context)







