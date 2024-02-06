from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list,  name = 'todo_list'),
    path('contact',views.contact, name = 'contact'),
    path('start',views.start, name ='start'),
]
