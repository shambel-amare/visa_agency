from django.forms import ModelForm
from .models import Application
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            "birth_date": AdminDateWidget(),
        }
