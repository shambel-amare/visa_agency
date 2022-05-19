from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name


class Agent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    company = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.first_name
