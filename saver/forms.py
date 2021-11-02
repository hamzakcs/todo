from django import forms
from django.forms import ModelForm
from .models import model


class form(ModelForm):
    class Meta:
        model = model
        fields = ('base',)
