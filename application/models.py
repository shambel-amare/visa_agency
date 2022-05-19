from datetime import datetime
from unicodedata import name
from xmlrpc.client import DateTime
from django.db import models
from accounts.models import User
import uuid

# Create your models here.

# APPLICANT_CHOICES=(

# )


class Application(models.Model):
    class ApplyType(models.IntegerChoices):
        BUSINESS = 1, "Business",
        WORK = 2, "Work",
        SCHOOL = 3, "School",
        MEDICAL = 4, "Medical",
        # (...)

    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(null=True)
    application_type = models.PositiveSmallIntegerField(
        choices=ApplyType.choices,
        default=ApplyType.WORK)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    Address = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_photo = models.ImageField(
        blank=True, null=True, upload_to="images/")

    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.first_name
