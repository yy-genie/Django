from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):
    context = {
        "form": LoginForm()
    }
    return render(request, 'accounts/login.html', context)