import django.contrib.messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
def todo_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            print('form is valid')
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todo_list')
    else:
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
