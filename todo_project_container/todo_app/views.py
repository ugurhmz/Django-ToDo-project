from django.shortcuts import render
from django.http import HttpResponse


def index(request):
      isim="Uğur HAMZAOĞLU"
      return render(request,"todo_pages/index.html", {'name':isim}) 


def about(request):
      return render(request, "todo_pages/about.html")