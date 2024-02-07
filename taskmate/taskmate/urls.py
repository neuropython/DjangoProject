
from django.contrib import admin
from django.urls import path, include
from todo_list_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('todo_list/', include('todo_list_app.urls')),
    path('contact', views.contact, name='contact'),
    path('start', views.start, name='start'),
]