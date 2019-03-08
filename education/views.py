from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, User
# Create your views here.
def home(request):
    return HttpResponse("Hello World!")
