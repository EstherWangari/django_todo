from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def todos(request):
    return render (request , "todos.html", {})


def form(request):

    if request.method =="GET":
        return render (request , "form.html" , {})

    else:
        title=request.POST["title"]
        description=request.POST["description"]
        due_date=request.POST["due_date"]
        
        print(title +""+description +"" +due_date)

        return HttpResponse ("Form submitted by" + title)

def Index(request):
    return render (request , "Index.html" , {})

def Login (request):
    return render (request , "Login.html" , {} )

def info(request):
    return render (request , "info.html" , {})

def staff (request):
    return render (request ,"staff.html" , {} )

def forms(request):
    return render (request , "forms.html" , {})



 