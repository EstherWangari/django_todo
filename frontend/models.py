from django.db import models
from   django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    TASK_PRIORITIES=(
        (LOW , "Low"),
        (MEDIUM , "Medium"),
        (HIGH , "High")

    )
    priority = models.CharField( max_length=20 , choices = TASK_PRIORITIES , default=LOW)
    complete = models.BooleanField(default= False)
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)
    ##Timestamps: They  record when a db was created and when it was last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





