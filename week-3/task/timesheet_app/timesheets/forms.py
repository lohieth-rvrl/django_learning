# timesheet/forms.py
from django import forms
from .models import Sheet

class createform(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = ['project', 'module', 'task', 'date', 'time', 'descreption']