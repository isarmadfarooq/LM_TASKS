from django.shortcuts import render, HttpResponseRedirect
from .forms import signUpForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


def sign_Up(request):
    if request.method == "POST":
        fm = signUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
        else:
            messages.error(request, 'Account Not Created. Something went wrong !!')
    else:
        fm = signUpForm()
    return render(request, 'enroll/signUp.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uName = fm.cleaned_data['username']
                uPass = fm.cleaned_data['password']
                user = authenticate(username=uName, password=uPass)
                login(request, user)
                messages.success(request, 'Logged in Successfully !!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Logged in Fail.Try Again !!')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userLogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change Successfully!!')
                return HttpResponseRedirect('/editprofile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change Successfully!!')
                return HttpResponseRedirect('/editprofile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def home(request):
    if request.user.is_authenticated:
        return render(request, "enroll/home.html")
    else:
        return HttpResponseRedirect('/login/')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userForm = CustomUserCreationForm(request.POST, instance=request.user)
            if userForm.is_valid():
                userForm.save()
                messages.success(request, 'Profile Updated !!')
        else:
            userForm = CustomUserCreationForm(instance=request.user)
        return render(request, 'enroll/userProfile.html', {'user_form': userForm, 'name': request.user.username})
    else:
        return HttpResponseRedirect('/login/')
