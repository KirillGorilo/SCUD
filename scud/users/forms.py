from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from .models import Student

class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        max_length=25,
        required=True,
    )
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        required=True,    
    )


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        label="Логин",
        max_length=25,
        required=True,
    )
    email = forms.CharField(
        label="E-mail", 
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
        required=True
    )
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        required=True,    
    )
    password2 = forms.CharField(
        label="Повторите пароль", 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
        required=True,    
    )

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = Student.objects.all()
        if user.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email