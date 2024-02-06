from django.shortcuts import render

def todo_list(request):
    content = {
        'todo_content': 'todo_content'
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
