import todolist
from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm

from .models import *

class TodolistForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = '__all__'
