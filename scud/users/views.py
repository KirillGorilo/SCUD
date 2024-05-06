from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect, HttpResponse
from users.forms import LoginUserForm, RegisterUserForm, SettingsForm
from django.urls import reverse
from .models import Student

def index(request):
   return render(request, "base.html")


def login_user(request):
   if request.method == 'POST':
      login_forms = LoginUserForm(request.POST)
      if login_forms.is_valid():
         cd = login_forms.cleaned_data
         user = authenticate(request, username=cd['username'], 
               password=cd['password'])
         if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
   else:
      login_forms = LoginUserForm()
   return render(request, 'users/login.html', {'login_forms': login_forms})

def logout_user(request):
   logout(request)
   return HttpResponseRedirect(reverse('login'))

def register(request):
   if request.method == "POST":
      form = RegisterUserForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password'])
         user.save()
         return HttpResponseRedirect(reverse('login'))
   else:
      form = RegisterUserForm()
   return render(request, 'users/register.html', {'register_form': form})

def settings(request):
   try:
      my_user = Student.objects.get(id=request.user.id)
   except DoesNotExist:
      return render(request, 'users/register.html', {'register_form': form})

   if request.method == "POST":
      form = SettingsForm(request.POST)
      if form.is_valid():
         new_username = form.cleaned_data['username']
         new_first_name = form.cleaned_data['first_name']
         new_last_name = form.cleaned_data['last_name']
         new_middle_name = form.cleaned_data['middle_name']
         # form.save()
         return HttpResponseRedirect(reverse('home'))

   form = SettingsForm()
   return render(request, 'users/settings.html', {'settings_form': form, 'my_user': my_user})