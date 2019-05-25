from django.http import HttpRequest
from django.shortcuts import render, redirect

def hello(request):
    return render(request, 'base.html')