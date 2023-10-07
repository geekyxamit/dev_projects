from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request
from .serializers import *
import datetime
from django.core.mail import EmailMultiAlternatives

# Create your views here.


class CreateAndViewUser(APIView):
    # method to view users
    def get(self, request, *args, **kwargs):
        data = request.GET
        user_obj = None
        ser_data = None
        if data.get("id"):
            user_obj = User.objects.filter(id=data["id"]).first()
            ser_data = UserSerializer(user_obj).data
        else:
            user_obj = User.objects.all()
            ser_data = UserSerializer(user_obj, many=True).data
        
        return Response({"user_data": ser_data,
                         "success": True})
    
    
    # method to create a new user
    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get("first_name") is None or data.get("first_name").strip() == "":
            return Response({"error": "First Name not given",
                             "success": False})
        
        if data.get("last_name") is None or data.get("last_name").strip() == "":
            return Response({"error": "Last Name not given",
                             "success": False})
        
        if data.get("email") is None or data.get("email").strip() == "":
            return Response({"error": "Email not given",
                             "success": False})
            
        ser_data = UserSerializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
        else:
            return Response({"error": ser_data.errors,
                             "success": False})
        return Response({"message": "User created successfully",
                         "success": True})
    


class CreateAndViewTask(APIView):
    
    # method to view tasks
    def get(self, request, *args, **kwargs):
        data = request.GET
        task_obj = Tasks.objects.all();
        
        if data.get("creator_id") is not None:
            task_obj = task_obj.filter(created_by=data["creator_id"])
            
        elif data.get("assignee_id") is not None:
            task_obj = task_obj.filter(assignee=data["assignee_id"])
            
        elif data.get("due_date") is not None:
            dd = datetime.datetime.strptime(data["due_date"], "%Y-%m-%d %H:%M:%S").date()
            task_obj = task_obj.filter(due_date__lte=dd)
        
        ser_data = TasksSerializer(task_obj, many=True).data
        return Response({"tasks_data": ser_data,
                         "success": True})
        
    
    
    # method to create a task
    def post(self, request, *args, **kwargs):
        data = request.data
        
        if data.get("task_title") is None or data.get("task_title").strip() == "":
            return Response({"error": "Task Title not given",
                             "success": False})
        
        if data.get("task_description") is None or data.get("task_description").strip() == "":
            return Response({"error": "Task Description not given",
                             "success": False})
            
        if data.get("due_date") is None:
            return Response({"error": "Task due date not given",
                             "success": False})
        
        if data.get("assignee_ids") is None:
            return Response({"error": "Task assignee IDs not given",
                             "success": False})
        
        if data.get("created_by") is None:
            return Response({"error": "Task creator not given",
                             "success": False})
        
        # check for duplicate task name
        task_objs = Tasks.objects.filter(task_title=data["task_title"]).first()
        # print(task_objs)
        if task_objs is not None:
            return Response({"error": "Task with this title already exist",
                             "success": False})
        
        data["due_date"] = datetime.datetime.strptime(data["due_date"], "%Y-%m-%d %H:%M:%S").date()
        # print(data["due_date"])
        
        unassigned_id_list = []
        email_receivers = []
        
        for assignee_id in data["assignee_ids"]:
            data["assignee"] = assignee_id
            # searching assignee user in DB
            assignee_obj  = User.objects.filter(id=assignee_id).first()
            
            if assignee_id == data["created_by"] or assignee_obj is None:
                # if creator and assignee is same, skip this id
                # if assignee with given id not found then skip this id
                unassigned_id_list.append(assignee_id)
                continue
            
            ser_data = TasksSerializer(data=data)
            if ser_data.is_valid():
                ser_data.save()
                # storing success assignee emails
                email_receivers.append(assignee_obj.email)
                
            else:
                # if serializer is invalid, then akip this id
                unassigned_id_list.append(assignee_id)
        
        
        # None of the assignee is valid, then task not created        
        if len(unassigned_id_list) == len(data["assignee_ids"]):
            return Response({"error": "Task not created",
                             "success": False})
        
        
        ## sending email to task assignees (smtp connection not established)
        
        # email_msg = "You have been assigned a task."
        # subject = "Task Assigned"
        # msg = EmailMultiAlternatives(subject, email_msg, "sender@gmail.com", [email_receivers])
        # msg.send()
        
        return Response({"message": "Task created successfully",
                         "unassigned_ids": unassigned_id_list,
                         "success": True})
        
         