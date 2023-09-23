from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from enroll.models import CustomUser


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(
            attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(
            attrs={"class": "form-control"})
    )


class CustomUserSignupForm(UserCreationForm):
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(
            attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(
            attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Last Name", widget=forms.TextInput(
            attrs={"class": "form-control"})
    )
    full_name = forms.CharField(
        label="Full Name", widget=forms.TextInput(
            attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser  # Replace with your user model
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "password1",
            "password2",
        ]
