from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Profile,Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {"projects":projects})

