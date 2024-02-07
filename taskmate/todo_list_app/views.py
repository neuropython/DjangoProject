import django.contrib.messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def todo_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            print('form is valid')
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todo_list')
    else:
        all_data = Task.objects.all()
        paginator = Paginator(all_data, 5)
        page = request.GET.get('pg')
        all_data = paginator.get_page(page)

        content = {
            'todo_content': all_data
        }
        return render(
            request, 'todo_list.html', content
        )

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ('Task Deleted!'))
    return redirect('todo_list')

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


def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    content = {
        'edit_task': task
    }
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST or None, instance= task)
    if form.is_valid():
        print('form is valid')
        form.save()
        return redirect('todo_list')
    messages.success(request, ('Task Edited!'))

    return render(
        request, 'edit.html', content
    )


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.complete = True
    task.save()
    messages.success(request, ('Task Completed!'))
    return redirect('todo_list')

def un_complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.complete = False
    task.save()
    messages.success(request, ('Task Completed!'))
    return redirect('todo_list')

def index(request):
    content = {
        'index_content': 'Index Content'
    }
    return render(
        request, 'index.html', content
    )

