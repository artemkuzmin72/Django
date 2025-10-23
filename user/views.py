from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from .models import Users as User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/register.html' 
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')

