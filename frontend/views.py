from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

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
    return render (request , "complete.html" , {})

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

 