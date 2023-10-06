from django.urls import path
from .views import *

urlpatterns = [
    # path('', views.index, name = 'home'),
    path('users/', CreateAndViewUser.as_view(), name="users_data"),
    path('tasks/', CreateAndViewTask.as_view(), name="tasks_data"),
    
]