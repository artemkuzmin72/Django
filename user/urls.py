from django.urls import path
from user.views import CustomLoginView
from user.views import RegisterView
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm
app_name = 'user'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]