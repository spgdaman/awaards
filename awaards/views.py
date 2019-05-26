from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Profile,Project
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-id')
    return render(request, 'index.html', {"projects":projects})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'projects' in request.GET and request.GET['projects']:
        search_term = request.GET.get('projects')
        search_item = Project.objects.filter(name__icontains=search_term)
        message=f"{{search_term}}"
        return render(request,'search.html',{"message":message,"projects":search_item})
    else:
        message="Please enter a correct search term"
        return render(request,"search.html")

def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    user_projects = Project.objects.filter(profile=profile_id)
    return render(request, 'profile.html', {"profiles":profile,"projects":user_projects})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    project = Project.objects.filter(id=project_id)
    return render(request,'project.html',{"projects":project})