from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list,  name = 'todo_list'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('un_complete/<task_id>', views.un_complete_task, name = "un_complete_task"),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('contact',views.contact, name = 'contact'),
    path('start',views.start, name ='start'),
]
