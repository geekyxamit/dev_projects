from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request
from .serializers import *

# Create your views here.


class CreateAndViewUser(APIView):
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
    
    def post(self, request, *args, **kwargs):
        data = request.data
        ser_data = UserSerializer(data=data)
        if ser_data.is_valid():
            ser_data.save()
        else:
            return Response({"error": ser_data.errors,
                             "success": False})
        return Response({"message": "User created successfully",
                         "success": True})
    
    