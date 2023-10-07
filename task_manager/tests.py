from django.test import TestCase

# Create your tests here.
from django.urls import reverse
import datetime
# from rest_framework import status
# from rest_framework.test import APITestCase
from .models import Tasks, CustomUser, TaskAssigneeMapping

class CreateAndViewTaskTests(TestCase):
    def setUp(self):
        self.creator_obj = CustomUser.objects.create(first_name= "karan", last_name= "Verma", email= "karanverma@gmail.com",
                                                     password= "Karan@123", age= 27)
        self.assignee_obj1 = CustomUser.objects.create(first_name= "Amit", last_name= "Sahu", email= "amitsahu@gmail.com",
                                                     password= "Amit@123", age= 27)
        self.assignee_obj2 = CustomUser.objects.create(first_name= "Raj", last_name= "Singh", email= "rajsingh@gmail.com",
                                                     password= "Raj@123", age= 27)
        
        self.task_obj = Tasks.objects.create(task_title='Task 1', task_description='Task desc 1', due_date='2023-10-14',
                                             created_by=self.creator_obj, created_at=datetime.datetime.now())
        self.task_obj_2 = Tasks.objects.create(task_title='Task 2', task_description='Task desc 2', due_date='2023-10-15',
                                             created_by=self.creator_obj, created_at=datetime.datetime.now())
        
        self.task_map_obj = TaskAssigneeMapping.objects.create(task=self.task_obj, assignee=self.assignee_obj1, task_status="open")
    
    def test_create_task(self):
        url = reverse('tasks_data')
        data = {"task_title": "Task demo 1",
                "task_description": "Task demo desc 1",
                "due_date": "2024-10-15 23:59:00",
                "assignee_ids": [self.assignee_obj1.id, self.assignee_obj2.id],
                "created_by": self.creator_obj.id}
        
        response = self.client.post(url, data=data, format='json')
        print(response)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        
        
    def test_view_tasks(self):
        url = reverse('tasks_data')
        params = {'assignee_id': self.assignee_obj1.id,
                  'due_date': '2023-10-15 23:59:00'}
        
        response = self.client.get(url, data=params)
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data['tasks_data']), 1)  # Assuming there's one existing task
        
    def test_view_tasks_2(self):
        url = reverse('tasks_data')
        params = {'due_date': '2023-10-14 23:59:00'}
        
        response = self.client.get(url, data=params)
        print(response.status_code)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        
