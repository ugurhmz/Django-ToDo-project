from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

def index(request):
      todo_list = Todos.objects.all()
    
      
      return render(request,"todo_pages/index.html",{'todo_list':todo_list}) 


def about(request):
      return render(request, "todo_pages/about.html")


def create(request):
      return render(request,"todo_pages/create.html")