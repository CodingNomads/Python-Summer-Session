# Tasks API Docs here: http://demo.codingnomads.co:8080/tasks_api/swagger-ui/index.html#/task-controller

import requests
import json

# Base URLs
BASE_USER_URL = "http://demo.codingnomads.co:8080/tasks_api/users"
BASE_TASK_URL = "http://demo.codingnomads.co:8080/tasks_api/tasks"

# Pretty printer for responses
def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:")
        print(json.dumps(response.json(), indent=4))
    except Exception:
        print("Response Text:")
        print(response.text)
    print("\n" + "="*50 + "\n")

# 1. Create a new user
print("POST Request - Create a New User")
new_user = {
    "email": "pythonista@codingnomads.com",
    "first_name": "Pythonista",
    "last_name": "Nomad"
}
response = requests.post(BASE_USER_URL, json=new_user)
print_response(response)

if response.status_code != 201:
    print("User creation failed. Exiting.")
    exit()

# Extract user ID
user_id = response.json()['data']['id']
print(f"New user ID: {user_id}")

# 2. Create a task using the user ID
print("POST Request - Create a Task for the New User")
sample_task = {
    "name": "Task for new user",
    "description": "Linked to the new user created above.",
    "completed": False,
    "userId": user_id
}
response = requests.post(BASE_TASK_URL, json=sample_task)
print_response(response)

if response.status_code != 201:
    print("Task creation failed. Exiting.")
    exit()

# Extract task ID
task_id = response.json()['data']['id']

# 3. GET - Retrieve all tasks for user
print("GET Request - Retrieve All Tasks for User")
response = requests.get(f"{BASE_USER_URL}/{user_id}/tasks")
print_response(response)

# 4. PUT - Fully update the task
print("PUT Request - Fully Update the Task")
updated_task = {
    "name": "Updated Task Title",
    "description": "Fully updated task description.",
    "completed": True,
    "userId": user_id  # must include userId for PUT
}
response = requests.put(f"{BASE_TASK_URL}/{task_id}", json=updated_task)
print_response(response)

# 5. PATCH - Partially update the task
print("PATCH Request - Partially Update the Task")
partial_update = {
    "name": "Partially Updated Title"
}
response = requests.patch(f"{BASE_TASK_URL}/{task_id}", json=partial_update)
print_response(response)

# 6. HEAD - Get headers only
print("HEAD Request - Headers for Task")
response = requests.head(f"{BASE_TASK_URL}/{task_id}")
print(f"Status Code: {response.status_code}")
print("Headers:", response.headers)
print("\n" + "="*50 + "\n")

# 7. OPTIONS - Check allowed HTTP methods
print("OPTIONS Request - Allowed Methods")
response = requests.options(BASE_TASK_URL)
print(f"Status Code: {response.status_code}")
print("Allowed Methods:", response.headers.get("Allow"))
print("\n" + "="*50 + "\n")

# 8. DELETE - Delete the task
print("DELETE Request - Delete the Task")
response = requests.delete(f"{BASE_TASK_URL}/{task_id}")
print_response(response)

# 9. Confirm task deletion
print("GET Request - Confirm Task Deletion")
response = requests.get(f"{BASE_TASK_URL}/{task_id}")
print_response(response)
