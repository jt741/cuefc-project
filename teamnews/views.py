from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from websitetext.models import AboutFives, Sponsors
from django.db.models import Q
from committee.models import Member

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

    mens_captain = Member.objects.all().filter(position="MC").order_by("-committee_start_year")[0]
    womens_captain = Member.objects.all().filter(position="WC").order_by("-committee_start_year")[0]
    mens_secretary = Member.objects.all().filter(position="MS").order_by("-committee_start_year")[0]
    womens_secretary = Member.objects.all().filter(position="WS").order_by("-committee_start_year")[0]
    welfare_officer = Member.objects.all().filter(position="WO").order_by("-committee_start_year")[0]
    junior_treasurer = Member.objects.all().filter(position="JT").order_by("-committee_start_year")[0]
    social_secretary = Member.objects.all().filter(position="SS").order_by("-committee_start_year")[0]
    webmaster = Member.objects.all().filter(position="W").order_by("-committee_start_year")[0]

    committee_members = {
        "mens_captain": mens_captain,
        "womens_captain": womens_captain,
        "mens_secretary": mens_secretary,
        "womens_secretary": womens_secretary,
        "welfare_officer": welfare_officer,
        "junior_treasurer": junior_treasurer,
        "social_secretary": social_secretary,
        "webmaster": webmaster
    }

    start_years=[]
    for value in committee_members.values():
        start_years.append(value.committee_start_year)
    most_recent_year = max(start_years)
    tenure = f"{most_recent_year}-{most_recent_year+1}"

    context = {
        **committee_members,
        "tenure": tenure
    }

    return render(request, 'committee/committee.html', context=context)


def sponsorship(request):
    text = get_object_or_404(Sponsors)
    template = 'teamnews/sponsorship.html'
    context = {'text': text}
    return render(request, template, context)

def newsdetail(request, newspost_id):
    detailnewspost = get_object_or_404(BlogPost, pk=newspost_id)
    return render(request, 'teamnews/newsdetail.html', {'newspost': detailnewspost})

def captains(request):

    mens_captain = Member.objects.all().filter(position="MC").order_by("-committee_start_year")[0]
    womens_captain = Member.objects.all().filter(position="WC").order_by("-committee_start_year")[0]

    context = {
        "mens_captain": mens_captain,
        "womens_captain": womens_captain
    }
    return render(request, 'teamnews/captains.html', context=context)