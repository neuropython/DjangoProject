from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
def register(request):
    if request.method == "POST":
        register_form = CustomUserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Created, Login to get started"))
            return redirect('register')
    else:
        register_form = CustomUserCreationForm()

    content = {
        "content": register_form
    }

    return render(
            request, 'register.html', content
        )
