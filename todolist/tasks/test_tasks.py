import requests

ENDPOINT = "http://127.0.0.1:8000/"

payload1 = {
    "title" : "Games2",
    "description" : "Fortnite",
    "due_date" : "2020-06-04",
    "resources" : ["computer"]
}

payload2 = {
    "title" : "Games7",
    "description" : "Blaba",
    "due_date" : "2020-06-04",
    "resources" : ["computer"]
}

def test_create_tasks():
    requests.post(ENDPOINT + "addTask/", json=payload1)
    get_task_response = requests.get(ENDPOINT + f"get/{payload1['title']}", verify=False)
    get_task_data = get_task_response.json()

    assert get_task_data["title"] == payload1["title"]
    assert get_task_data["description"] == payload1["description"]
    assert get_task_data["due_date"] == payload1["due_date"]
    assert get_task_data["resources"] == payload1["resources"]


def test_update_task_to_completed():
    uncomplete_task = requests.post(ENDPOINT + "addTask/", json=payload1)
    uncomplete_task_title = uncomplete_task.json()["title"]
    updated_task = requests.patch(ENDPOINT + f"tasks/{uncomplete_task_title}/")
    assert updated_task.json()["completed"] == True


def test_delete_task():
    task = requests.post(ENDPOINT + "addTask/", json=payload2)
    task_title = task.json()["title"]
    assert task_title == payload2["title"]
    delete_task_response = requests.delete(ENDPOINT + f"tasks/{task_title}/")
    assert delete_task_response.status_code == 204
    response = requests.get(ENDPOINT + f"get/{task_title}/")
    assert response.status_code == 404


def test_get_all_uncompleted_tasks():
    uncompleted_tasks = requests.get(ENDPOINT + "todoTasks/")
    for task in uncompleted_tasks.json():
        assert task["completed"] == False 
