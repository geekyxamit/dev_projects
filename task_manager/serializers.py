from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
        

class TaskAssigneeMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssigneeMapping
        fields = "__all__"
    