from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Profile,Project
from django.contrib.auth.decorators import login_required
from .forms import NewProject,UpdateProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Project
from .serializers import ProfileSerializer,ProjectSerializer 

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

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    user_projects = Project.objects.filter(profile=profile_id)
    return render(request, 'profile.html', {"profiles":profile,"projects":user_projects})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')
    else:
        form = UpdateProfile()
    return render(request,'updateprofile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    project = Project.objects.filter(id=project_id)
    return render(request,'project.html',{"projects":project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProject(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = NewProject()
    return render(request,'newproject.html', {"form":form})

class ProfileDetails(APIView):
    def get(self, request, format=None):
        all_profiles=Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectDetails(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)