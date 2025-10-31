from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
  return render(request, "home.html", {})

def profile(request):
  return HttpResponse("this profile page viji")