from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from .models import User

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
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.all()
        if user.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class SettingsForm(forms.ModelForm):
    username = forms.CharField(
        label="Логин",
        max_length=20,
        min_length=3,
        required=False,
    )
    last_name = forms.CharField(
        label="Фамилия",
        max_length=20,
        min_length=3,
        required=False,
    )
    first_name = forms.CharField(
        label="Имя",
        max_length=20,
        min_length=3,
        required=False,
    )
    middle_name = forms.CharField(
        label="Отчество",
        max_length=25,
        min_length=3,
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        middle_name = cleaned_data.get('middle_name')

        if last_name == '':
            if self.instance and self.instance.last_name:
                cleaned_data['last_name'] = self.instance.last_name

        if first_name == '':
            if self.instance and self.instance.first_name:
                cleaned_data['first_name'] = self.instance.first_name

        if middle_name == '':
            if self.instance and self.instance.middle_name:
                cleaned_data['middle_name'] = self.instance.middle_name

        if username == '':
            if self.instance and self.instance.username:
                cleaned_data['username'] = self.instance.username

        return cleaned_data

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "middle_name")