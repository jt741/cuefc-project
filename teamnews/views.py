from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from websitetext.models import AboutFives
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
    # return render(request, 'committee/committee.html') #idk why but it auto goes to committee even if u type teamnews!
    sorted_members = Member.objects.all().order_by("-committee_start_year")
    most_recent_year = sorted_members[0].committee_start_year
    most_recent_committee = Member.objects.all().filter(committee_start_year=most_recent_year)


    mens_captain = get_object_or_404(most_recent_committee, position="MC")
    womens_captain = get_object_or_404(most_recent_committee, position="WC")
    mens_secretary = get_object_or_404(most_recent_committee, position="MS")
    womens_secretary = get_object_or_404(most_recent_committee, position="WS")
    welfare_officer = get_object_or_404(most_recent_committee, position="WO")
    junior_treasurer = get_object_or_404(most_recent_committee, position="JT")
    social_secretary = get_object_or_404(most_recent_committee, position="SS")
    webmaster = get_object_or_404(most_recent_committee, position="W")

    context = {
        "mens_captain": mens_captain,
        "womens_captain": womens_captain,
        "mens_secretary": mens_secretary,
        "womens_secretary": womens_secretary,
        "welfare_officer": welfare_officer,
        "junior_treasurer": junior_treasurer,
        "social_secretary": social_secretary,
        "webmaster": webmaster
    }
    return render(request, 'committee/committee.html', context=context)


def sponsership(request):
    return render(request, 'teamnews/sponsership.html')

def newsdetail(request, newspost_id):
    detailnewspost = get_object_or_404(BlogPost, pk=newspost_id)
    return render(request, 'teamnews/newsdetail.html', {'newspost': detailnewspost})

def captains(request):
    sorted_members = Member.objects.all().order_by("-committee_start_year")
    most_recent_year = sorted_members[0].committee_start_year
    most_recent_committee = Member.objects.all().filter(committee_start_year=most_recent_year)

    mens_captain = get_object_or_404(most_recent_committee, position="MC")
    womens_captain = get_object_or_404(most_recent_committee, position="WC")

    context = {
        "mens_captain": mens_captain,
        "womens_captain": womens_captain
    }
    return render(request, 'teamnews/captains.html', context=context)