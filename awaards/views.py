from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Profile,Project
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects":projects})

@login_required(login_url='/accounts/login/')
@csrf_protect
def search_results(request):
    c={}
    if 'projects' in request.GET and request.GET['[projects]']:
        search_term = request.GET.get('projects')
        search_item = Project.objects.filter(name__icontains=search_term)
        message=f"{{search_term}}"
        return render(request,'search.html',{"message":message,"projects":search_item},c)
    else:
        message="Please enter a correct search term"
        return render(request,"search.html",c)

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    return render(request, 'profile.html', {"profiles":profile})