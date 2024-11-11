from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to Blog Home</h2>")

def about(request):
    return HttpResponse("<h2>About Blog</h2>")