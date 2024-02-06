from django.shortcuts import render
from .models import Task

def todo_list(request):

    all_data = Task.objects.all
    content = {
        'todo_content': all_data
    }
    return render(
        request, 'todo_list.html', content
    )

def contact(request):
    content = {
        'contact_content': 'contact_content'
    }
    return render(
        request, 'contact.html', content
    )

def start(request):
    content = {
        'start_content': 'start_content'
    }
    return render(
        request, 'start.html', content
    )
