from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
from django.core.mail import send_mail

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Users
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)
        # Отправка письма после успешной регистрации
        if commit:
            send_mail(
                subject="Добро пожаловать!",
                message="Вы успешно зарегистрировались в системе.",
                from_email=None,  # можно указать settings.DEFAULT_FROM_EMAIL
                recipient_list=[user.email],
            )
        return user

class CustomAuthenticationForm(AuthenticationForm):
    pass
