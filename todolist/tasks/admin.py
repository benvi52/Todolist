from django_mongoengine import mongo_admin
from .models import Task

mongo_admin.site.register(Task)
