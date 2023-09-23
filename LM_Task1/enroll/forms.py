from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class signUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

    def __init__(self, *args, **kwargs):
        super(signUpForm, self).__init__(*args, **kwargs)

        # Add custom CSS classes to each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profile_picture', 'first_name',
                                                 'last_name', 'email', 'date_joined', 'last_login',
                                                 'phone_number', 'address')
