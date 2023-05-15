from  django.urls import path
from . import views

urlpatterns = [
    path('allTasks/', views.get_all_tasks),
    path('addTask/', views.create_a_task),
    path('tasks/<title>/', views.update_task),
    path('todoTasks/', views.get_to_do_tasks),
    path('get/<title>/', views.get_one_task)
]
