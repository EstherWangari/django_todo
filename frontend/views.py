from dataclasses import fields
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView , UpdateView 

from frontend.models import Task

# Create your views here.


def mains(request):
    return render (request , "main.html", {})


def form(request):

    if request.method =="GET":
        return render (request , "form.html" , {})

    else:
        title=request.POST["title"]
        description=request.POST["description"]
        due_date=request.POST["due_date"]
        
        print(title +""+description +"" +due_date)

        return HttpResponse ("Form submitted by" + title)

def index(request):
    return render (request , "index.html" , {})

def login (request):
        
    name = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, name=username, password=password);user

    if user is not None:
         name = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, name=username, password=password);user

    login(request, user)
         # Redirect to a success page....
         # Return an 'invalid login' error message. ...

    return render (request , "login.html" , {} )

def complete(request):
    todos= Task.objects.filter(complete=True)
    context = {
        "todos" : todos
    }

    return render (request , "complete.html" , context)

def pending (request):
    todos = Task.objects.filter (complete= False )
    context = {
        "todos" : todos
    }

    return render (request , "complete.html" , context)

def staff (request):
    return render (request ,"staff.html" , {} )

def forms(request):
    return render (request , "forms.html" , {})

def todos(request):
    return render (request , "todos.html", {})

def task_form(request):
    return render (request , "task_form" , {})

def complete_blog (request):
    return render (request , "complete_blog" , {})

def complete_bowl(request):
    return render (request , "complete_bowl" , {})

def complete_manage (request):
    return render (request , "complete_manage" , {})


def task_details (request , id ):
    task = Task.objects.filter( pk=id ).first()
    context={
        "task" : task
    }

    if task is complete:
        task.save()
        return render('task_details.html')

    if request.method =="POST":
        task = TaskUpdate(request.POST,instance=task)
        return render (request , "task_details.html" , context)
    
    return render(request , "task_details.html" , {})

class TaskCreate(CreateView):
    model = Task
    template_name = "task_form.html"
    fields=["title" , "description", "due_date", "priority"]
    success_url = "/pending"


class TaskUpdate(UpdateView):
    model = Task
    template_name = "task_details.html"
    fields=["complete"]
    success_url = "/pending"

