from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        print("Save method is being called!")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        self.full_name = f"{self.first_name} {self.last_name}"
        print("Full Name:", self.full_name)
        super().save(*args, **kwargs)