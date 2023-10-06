from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request

# Create your views here.


class CreateAndViewUser(APIView):
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        data = request.data
        
    
    