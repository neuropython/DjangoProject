import django.contrib.messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        user = request.user
        print(user)
        if form.is_valid():
            print('form is valid')
            form.save(commit=False).user = user
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todo_list')
    else:
        all_data = Task.objects.filter(user=request.user)
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
    if task.user == request.user:
        task.delete()
        messages.success(request, ('Task Deleted!'))
    else:
        messages.error(request, ('Access Restricted!'))
    return redirect('todo_list')

@login_required
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
    if task.user == request.user:
        task.complete = True
        messages.success(request, ('Task Completed!'))
        task.save()
    else:
        messages.error(request, ('Access Restricted!'))
    return redirect('todo_list')

def un_complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.user == request.user:
        task.complete = False
        messages.success(request, ('Task do not completed!'))
        task.save()
    else:
        messages.error(request, ('Access Restricted!'))
    return redirect('todo_list')

def index(request):
    content = {
        'index_content': 'Index Content'
    }
    return render(
        request, 'index.html', content
    )

