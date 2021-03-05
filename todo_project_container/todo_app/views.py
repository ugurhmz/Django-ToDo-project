from django.shortcuts import render
from django.http import HttpResponse


def index(request):
      
      return render(request,"todo_pages/index.html") 


def about(request):
      return render(request, "todo_pages/about.html")


def create(request):
      return render(request,"todo_pages/create.html")