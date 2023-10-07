from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    
    USERNAME_FIELD = 'email'

class Tasks(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    due_date = models.DateField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="task_creator")
    
class TaskAssigneeMapping(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="assigned_task")
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assigned_to")
    