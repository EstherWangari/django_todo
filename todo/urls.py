"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from frontend.views import TaskCreate, form,mains,index,login ,todos, staff ,forms ,complete, task_form,task_details,pending
from django.contrib.auth import authenticate, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',form, name="form_page"),
    path('' ,index, name="index_page"),
    path('todos/', mains, name="mains_page"),
    path('login/' , login , name="login_page"),
    path('complete/', complete , name ="complete"),
    path('staff/' , staff , name="staff_page"),
    path('forms/' , forms , name="forms_page"),
    path('task/form' , TaskCreate.as_view() , name="task.form"),
    path('pending/' , pending , name="pending"),
    path('task/details/<id>' , task_details , name="task.details"),
    
]
