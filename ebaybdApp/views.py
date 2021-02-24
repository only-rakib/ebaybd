from django.shortcuts import render, get_object_or_404
from . models import *


def home_view(request):
    news_list = Recent_News.objects.all()
    return render(request, 'home.html',{'news':news_list})


def project_view(request, title):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = get_object_or_404(Projects, slug=title)
    photos = Image_for_projects.objects.filter(modelForImage=project_list)
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def covid19_view(request):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = Covid19.objects.first()
    photos = Image_for_covid19.objects.all()
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def donate_view(request, title):
    donate_list = Donate.objects.get(slug=title)
    # print(project_list)
    return render(request, 'projects.html', {'context': donate_list})

def aboutus_view(request, title):
    aboutus_list = About_Us.objects.get(slug=title)
    # print(project_list)
    return render(request, 'projects.html', {'context': aboutus_list})

def committee_view(request, title):
    committee=""
    page_title=""
    if title == "advisor":
        page_title="উপদেষ্ঠা"
        committee = AdvisorCommittee.objects.all()
    elif title == "executive":
        page_title="কার্যকরী কমিটি"
        committee = ExecutiveCommittee.objects.all()
        
    else:
        page_title="স্বেচ্ছাসেবক"
        committee = VolunteerCommittee.objects.all()
    return render(request,'committee.html',{'context':committee,'title':page_title})

def contactus_view(request):
    return render(request, 'contactus.html')
def photo_gallery_view(request):
    photos = Image_for_Photo_Gallery.objects.all()
    project_title={
        'project_title':"ফটো গ্যালারী",
    }
    return render(request, 'projects.html', {'context': project_title, 'photos': photos})

def video_gallery_view(request):
    videos = Link_for_Video_Gallery.objects.all()
    project_title={
        'project_title':"ভিডিও গ্যালারী",
    }
    return render(request, 'projects.html', {'context': project_title, 'videos': videos})

def recent_news_view(request):
    news_list = Recent_News.objects.all()
    return render(request, 'pressbriefing.html',{'news':news_list})

def news_view(request,title):
    news_list = Recent_News.objects.all().exclude(slug=title)
    news = get_object_or_404(Recent_News, slug=title)
    return render(request, 'news.html',{'news':news,'sug':news_list})