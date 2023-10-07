from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        
class TasksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ('id', 'task_title', 'task_description', 'due_date', 'created_by')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        assignee_mapping = TaskAssigneeMapping.objects.filter(task=instance).\
            values_list('assignee', flat=True)
            
        data['assignee'] = assignee_mapping 
        return data
      

class AssignedTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
        

class CreatedTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id', 'task_title', 'task_description', 'due_date')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)
        assignee_mapping = TaskAssigneeMapping.objects.filter(task=instance).\
            values_list('assignee', flat=True)
            
        data['assignee'] = assignee_mapping 
        return data 
   

class TaskAssigneeMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssigneeMapping
        fields = "__all__"
    
