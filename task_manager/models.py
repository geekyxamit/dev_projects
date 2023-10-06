from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, unique=True)
    age = models.IntegerField(null=True)

class Tasks(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    due_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_creator")
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_assignee")
    
