from dataclasses import fields
from pyexpat import model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login 
from django.views.generic.edit import CreateView , UpdateView 
from django.contrib.auth.models import User 
from django.db import models 
from django.contrib import messages
from frontend.models import Task 

# Create your views here.

def sidebar (request):
    return render (request, "sidebar.html" , {})

def dashboard(request):

    pending_count = Task.objects.filter(complete=False).count()
    complete_count = Task.objects.filter(complete=True).count()

    context = {
        "pending": pending_count,
        "complete": complete_count

    }
    return render (request, "dashboard.html" , context)

def home(request):
    return render (request, "home.html", {})



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

def login_user (request):

    if request.method == "GET":
        return render(request , "registration/Login.html" , {} )
        
    
    name = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=name, password=password)

    if not user:
        message = "User not authenticated. Please make sure you are using the correct credentials. Or register the user."
        messages.info (request , message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    login(request, user)
         # Redirect to a success page....
         # Return an 'invalid login' error message. ...

    return HttpResponseRedirect("/pending")



def complete(request):
    ##  You will need to get the todos belonging to a particular user. 
    # We can get the user through the request. 
    # After accessing the user, then we add a condition into the filter of Task.objects.filter(complete=True, ....additional condition for user)

 
    todos= Task.objects.filter(complete=True)

    if request.method == "POST":
        if "Add_task" in request.POST:
            title = request.POST["description"]
            due_date = str(request.POST["due_date"])
            id = request.POST["id_select"]
            category = request.POST["category_select"]


            content = title + " -- " + due_date + " " + id
            Todo = Task( user= request.user, title=title, content=content, due_date=due_date, id=id,
            category=category.objects.get(name=category))
            Todo.save()

            return HttpResponseRedirect("/complete")

    context = {
        "todos" : todos
    }

    return render (request , "complete.html" , {"todos": todos} )

def pending (request):
    todos = Task.objects.filter (complete= False )

    if request.method == "POST":
        if "Add_task" in request.POST:
            title = request.POST["description"]
            due_date = str(request.POST["due_date"])
            category = request.POST["category_select"]


            content = title + " -- " + due_date + " " 
            Todo = Task(title=title, content=content, due_date=due_date, category=category.objects.get(name=category))
            Todo.save()

            return HttpResponseRedirect("/pending")
    context = {
        "todos" : todos
    }

    return render (request , "complete.html" , context)

def register(request):
    
    if request.method=="GET":

        return render (request , "register.html" , {})

    else :
        username = request.POST['username']  
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST.get('confirm_password')

        ##Check if username or email exists
        user_exists = User.objects.filter(username__iexact = username)
        if user_exists:

            messages.info(request, 'Username already exists.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        email_exists = User.objects.filter(email__iexact = email)
        if email_exists:

            messages.info(request, 'Email already exists.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        if password != confirm :
            messages.info(request , 'Passwords do not match.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        user = User.objects.create_user(username , email , password)

        login(request, user)
                # Redirect to a success page....
                # Return an 'invalid login' error message. ...

        return HttpResponseRedirect("/pending")



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

    if request.method =="POST":
        task = TaskUpdate(request.POST,instance=task)
        return render (request , "task_details.html" , context)
    
    return render(request , "task_details.html" , context)

def update_task_status(request, id):
    #1. Get the task
    #2. Check whether task is complete or not
    #3. If not complete change from pending to complete (task.complete = True)
    #4. Save the updated task (task.save())
    #5. Redirect someone to the complete view

    ##Here we are getting the task from the Database using the ID.
    task = Task.objects.filter(pk=id).first()

    ## Here we add the task to the context variable
    context = {
        "task" : task
    }

    ## If task is not complete: This condition should allow us to change the complete status of the task
    if task.complete != True :
        task.complete = True
        ## Updated task should be saved
        task.save()
        ## The task_details should be returned 
        return HttpResponseRedirect('/complete')

    ## If task is completed, then should be directed to complete.html
    else:
        return HttpResponseRedirect('/complete')


    



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

