from rest_framework_mongoengine import serializers
from .models import Task

class TaskSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "completed", "resources"]