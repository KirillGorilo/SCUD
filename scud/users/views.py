from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect, HttpResponse
from users.forms import LoginUserForm, RegisterUserForm
from django.urls import reverse

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
