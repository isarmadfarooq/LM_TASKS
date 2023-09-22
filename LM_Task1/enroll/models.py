from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(default="", validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(default="", max_length=255)
    profile_picture = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return str(self.username)
