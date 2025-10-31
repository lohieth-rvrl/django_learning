from django import forms
from . import models

class addForm(forms.ModelForm):
    class Meta:
        model = models.todos
        fields = ['title', 'description', 'date', 'priority', 'status']
        widgets = {
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }