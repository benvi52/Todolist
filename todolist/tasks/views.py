from dotenv import load_dotenv, find_dotenv
import os
from pymongo.mongo_client import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from bson.objectid import ObjectId
from rest_framework import status


load_dotenv(find_dotenv())
password = os.environ.get("PWD")
my_client = MongoClient(f"mongodb+srv://benvila52:Jordan52@todolist.8om2pod.mongodb.net/")

todolist = my_client.todolist
tasks = todolist.tasks

@api_view(['GET'])
def get_all_tasks(request):
    all_tasks = tasks.find()
    ser = TaskSerializer(all_tasks, many=True)
    return Response(ser.data)

@api_view(["GET"])
def get_to_do_tasks(request):
    tasks_to_do = tasks.find({"completed" : False})
    ser = TaskSerializer(tasks_to_do, many=True)
    return Response(ser.data)

@api_view(["GET"])
def get_one_task(request, title):
    task = tasks.find_one({"title" : title})
    if task is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ser = TaskSerializer(task)
    return Response(ser.data) 
    

@api_view(['POST'])
def create_a_task(request):
    _id = tasks.insert_one(request.data).inserted_id
    completed = {
        "$set" : {"completed" : False}
    }
    tasks.update_one({"_id":_id}, completed)
    task = tasks.find_one({"_id" : _id})
    ser = TaskSerializer(task)
    return Response(ser.data)

@api_view(["PATCH", "DELETE"])
def update_task(request, title):
    if request.method == "PATCH":
        update = {
            "$set" : {"completed" : True}
        }
        tasks.update_one({'title': title}, update)
        task = tasks.find_one({"title" : title})
        ser = TaskSerializer(task)
        return Response(ser.data) 
    
    elif request.method == "DELETE":
        tasks.delete_one({"title" : title})
        return Response(status=status.HTTP_204_NO_CONTENT)
    

