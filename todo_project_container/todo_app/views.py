from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos
from .forms import ListForm

def index(request):
      if request.method =="POST":
            form = ListForm(request.POST or None)

            if form.is_valid: #form validse kaydet
                  form.save()
                  todo_list = Todos.objects.all()
                  return render(request,"todo_pages/index.html",{'todo_list':todo_list}) 


      else:
            todo_list = Todos.objects.all()
            return render(request,"todo_pages/index.html",{'todo_list':todo_list}) 

      

def about(request):
      return render(request, "todo_pages/about.html")


def create(request):
      if request.method =="POST":
            form = ListForm(request.POST or None)

            if form.is_valid: #form validse kaydet
                  form.save()
                  todo_list = Todos.objects.all()
                  return render(request,"todo_pages/create.html",{'todo_list':todo_list}) 


      else:
            todo_list = Todos.objects.all()
            return render(request,"todo_pages/create.html",{'todo_list':todo_list}) 



def delete(request,Todos_id):
      todo = Todos.objects.get(pk=Todos_id)
      todo.delete()
      return redirect("index") #silme olunca yönlendir-> redirect ile, index page

def no_finish(request,Todos_id):
      todo = Todos.objects.get(pk = Todos_id)
      todo.finished = True
      todo.save()
      return redirect("index")


def yes_finish(request,Todos_id):
      todo = Todos.objects.get(pk = Todos_id)
      todo.finished =  False
      todo.save()
      return redirect("index")

def update(request,Todos_id):
      if request.method =="POST":
            todo_list = Todos.objects.get(pk=Todos_id)
            form = ListForm(request.POST or None, instance=todo_list)

            if form.is_valid: #form validse kaydet
                  form.save()
                  return redirect("index")


      else:
            todo_list = Todos.objects.all()
            return render(request,"todo_pages/update.html",{'todo_list':todo_list}) 