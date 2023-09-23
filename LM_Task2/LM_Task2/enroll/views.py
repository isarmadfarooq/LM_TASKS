from django.contrib.auth import logout
from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserLoginForm, CustomUserSignupForm


def custom_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def custom_signup(request):
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
    else:
        form = CustomUserSignupForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return HttpResponseRedirect('/login/')
