from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from users.forms import LoginUserForm, RegisterUserForm, SettingsForm
from django.urls import reverse
from .models import User


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
        my_user = User.objects.get(id=request.user.id)
    except:
        return render(request, "base.html")

    if request.method == "POST":
        form = SettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            # my_user.first_name = form.cleaned_data['first_name']
            # my_user.middle_name = form.cleaned_data['middle_name']
            # my_user.last_name = form.cleaned_data['last_name']
            # my_user.save()
            form.save()
            return render(request, 'users/settings.html', {'form': form, 'user': my_user})
        else:
            return render(request, 'users/settings.html', {'form': form})
    else:
        form = SettingsForm()

    return render(request, 'users/settings.html', {'form': form})
