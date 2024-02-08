from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def register(request):
    register_form = UserCreationForm()
    content = {
        "content": register_form
    }

    return render(
            request, 'register.html', content
        )
