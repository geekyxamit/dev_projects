Task Manager


# All the APIs are tested on localhost server.
# Create a virtual environment and install dependencies given in requirements.txt file.

1. To create and view all users
Base Url - ‘http://127.0.0.1:8000/users’
> To view all users:
        Method - GET
Url - “http://127.0.0.1:8000/users”
        Params - none
        Expected Output




{   
 "user_data": [
        {
            "id": 1,
            "password": "Aj@123",
            "last_login": null,
            "first_name": "AJ",
            "last_name": "Styles",
            "email": "ajstyles@gmail.com",
            "age": 32
        },
        {
            "id": 2,
            "password": "Amit@123",
            "last_login": null,
            "first_name": "Amit",
            "last_name": "Sahu",
            "email": "amitsahu@gmail.com",
            "age": 23
        }
],
    "success": true
}




# I have used the AbstractBaseUser Class of Django for Storing Users. Since we are not dealing with login and authentication. We have not encrypted the password.






> To view a user with given id:
        Method - GET
Url - “http://127.0.0.1:8000/users?id=1”
        Params - “id=<ID>”
        Expected Output 
                
{
    "user_data": {
        "id": 1,
        "password": "Aj@123",
        "last_login": null,
        "first_name": "AJ",
        "last_name": "Styles",
        "email": "ajstyles@gmail.com",
        "age": 32
    },
    "success": true
}






> to create a new user
        Method - POST
Url - “http://127.0.0.1:8000/users/”
        Body = {
    "first_name": "Kk",
    "last_name" : "Singh",
    "email": "kksingh@gmail.com",
    "password": "Kk@123",
    "age": 27
}

        Expected Output
{
    "message": "User created successfully",
    "success": true
}








2. To create and View Tasks
Base url - “http://127.0.0.1:8000/tasks”


> to view all tasks
        Method - GET
Url - “http://127.0.0.1:8000/tasks”
        Params - None
        Expected Output


{
    "tasks_data": [
        {
            "id": 1,
            "task_title": "Task 1",
            "task_description": "Task desc 1",
            "due_date": "2023-10-13",
            "created_by": 2,
            "assignee": [
                1,
                3
            ]
        },
        {
            "id": 2,
            "task_title": "Task 2",
            "task_description": "Task desc 2",
            "due_date": "2023-10-13",
            "created_by": 1,
            "assignee": [
                2,
                3
            ]
        },
        {
            "id": 3,
            "task_title": "Task 3",
            "task_description": "Task desc 3",
            "due_date": "2023-10-13",
            "created_by": 1,
            "assignee": [
                3
            ]
        }
    ],
    "page_number": 1,
    "success": true
}


# The data is paginated and 1 page shows 3 entries. 
# to view data at a particular page, pass page as param in this way:
                Url - “http://127.0.0.1:8000/tasks?page=2”

> to filter tasks assigned to a given user
Method - GET
Url - “http://127.0.0.1:8000/tasks?assignee_id=2”
        Params - “assignee_id=<ID>”
        Expected Output
{
    "tasks_data": [
        {
            "id": 2,
            "task_title": "Task 2",
            "task_description": "Task desc 2",
            "due_date": "2023-10-13",
            "created_at": "2023-10-07T18:09:53.556670Z",
            "created_by": 1
        },
        {
            "id": 5,
            "task_title": "Task 4",
            "task_description": "Task desc 4",
            "due_date": "2023-10-13",
            "created_at": "2023-10-07T18:09:53.556670Z",
            "created_by": 3
        }
    ],
    "page_number": 1,
    "success": true
}


# you can also filter the output to view tasks having due date less than or equal to a given due date.
Url - “http://127.0.0.1:8000/tasks?assignee_id=2&due_date=2023-10-13 23:59:00”

> to filter tasks created by a given user
Method - GET
Url - “http://127.0.0.1:8000/tasks?creator_id=2”
        Params - “creator_id=<ID>”
        Expected Output
{
    "tasks_data": [
        {
            "id": 1,
            "task_title": "Task 1",
            "task_description": "Task desc 1",
            "due_date": "2023-10-13",
            "assignee": [
                1,
                3
            ]
        },
        {
            "id": 6,
            "task_title": "Task4",
            "task_description": "task desc 4",
            "due_date": "2023-10-13",
            "assignee": [
                1,
                3
            ]
        },
        {
            "id": 7,
            "task_title": "task4",
            "task_description": "task desc 4",
            "due_date": "2023-10-13",
            "assignee": [
                1,
                3
            ]
        }
    ],
    "page_number": 1,
    "success": true
}


# you can also filter the output to view tasks having due date less than or equal to a given due date.
Url - “http://127.0.0.1:8000/tasks?creator_id=2&due_date=2023-10-13 23:59:00”



> to view tasks having due date equal or less than a given date
        Method - GET
Url - “http://127.0.0.1:8000/tasks?due_date=2023-10-14 23:59:00”
        Params - “due_date=<DATETIME_STRING>”
        Expected Output
        
   {
 "tasks_data": [
        {
            "id": 1,
            "task_title": "Task 1",
            "task_description": "Task desc 1",
            "due_date": "2023-10-13",
            "created_by": 2,
            "assignee": [
                1,
                3
            ]
        },
        {
            "id": 2,
            "task_title": "Task 2",
            "task_description": "Task desc 2",
            "due_date": "2023-10-13",
            "created_by": 1,
            "assignee": [
                2,
                3
            ]
        },
        {
            "id": 3,
            "task_title": "Task 3",
            "task_description": "Task desc 3",
            "due_date": "2023-10-13",
            "created_by": 1,
            "assignee": [
                3
            ]
        }
    ],
    "page_number": 1,
    "success": true
}


> to create a task and assign it to user(s).
Method - POST
Url - “http://127.0.0.1:8000/tasks/”
        Body = {
    "task_title": "Task 6",
    "task_description": "task desc 6",
    "due_date": "2023-10-14 23:59:00",
    "created_by": 3,
    "assignee_ids": [1,2]
}

        Expected Output
{
    "message": "Task created successfully",
    "unassigned_ids": [],
    "success": true
}


# if one or more assignee id(s) is/are not found or invalid then this/these id(s) will be returned in ‘unassigned_ids’ list.

# if task is assigned to none of the assignee, then task will not be created. You will receive an output like :
{
    "error": "Task not created",
    "success": false
}





> to delete a task
Method - DELETE
Url - “http://127.0.0.1:8000/tasks/”
        Body = {
    "id": 9
}
Expected Output
{
    "message": "Task deleted",
    "success": true
}