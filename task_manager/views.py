from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request
from .serializers import *
import datetime

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
        pass
    
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
        
        data["due_date"] = datetime.datetime.strptime(data["due_date"], "%Y-%m-%d %H:%M:%S").date()
        
        unassigned_id_list = []
        
        for assignee_id in data["assignee_ids"]:
            data["assignee"] = assignee_id
            # searching assignee user in DB
            assignee_obj  = User.objects.filter(id=assignee_id).first()
            
            if assignee_obj is None:
                # if assignee with given id not found then skip this id
                unassigned_id_list.append(assignee_id)
                continue
            
            ser_data = TasksSerializer(data=data)
            if ser_data.is_valid():
                ser_data.save()
            else:
                # if serializer is invalid, then akip this id
                unassigned_id_list.append(assignee_id)
                
        return Response({"message": "Task created successfully",
                         "unassigned_ids": unassigned_id_list,
                         "success": True})