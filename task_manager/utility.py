
from django.core.paginator import Paginator


# function to validate given user_data
def validate_userdata(data):
    if data.get("first_name") is None or data.get("first_name").strip() == "":
        return {"error": "First Name not given",
                            "success": False}
    
    if data.get("last_name") is None or data.get("last_name").strip() == "":
        return {"error": "Last Name not given",
                            "success": False}
    
    if data.get("email") is None or data.get("email").strip() == "":
        return {"error": "Email not given",
                            "success": False}
    if data.get("password") is None or data.get("password").strip() == "":
        return {"error": "Password not given",
                            "success": False}
    
    return "OK"



# function to validate given task_data
def validate_taskdata(data):
    
    if data.get("task_title") is None or data.get("task_title").strip() == "":
        return {"error": "Task Title not given",
                            "success": False}
    
    if data.get("task_description") is None or data.get("task_description").strip() == "":
        return {"error": "Task Description not given",
                            "success": False}
        
    if data.get("due_date") is None:
        return {"error": "Task due date not given",
                            "success": False}
    
    if data.get("assignee_ids") is None:
        return {"error": "Task assignee IDs not given",
                            "success": False}
    
    if data.get("created_by") is None:
        return {"error": "Task creator not given",
                            "success": False}

    return "OK"


# function to paginate the data
def pagi(data, task_obj):
    obj_per_page = data.get("per_page") if data.get("per_page") else 3
    page_number = data.get("page") if data.get("page") else 1
    
    paginator = Paginator(task_obj, per_page=obj_per_page)
    page_object = paginator.get_page(page_number)
    return {"obj":page_object,
            "page_number": page_number}
