from django import forms
from .models import Article

class create_articleform(forms.ModelForm):
    class Meta:
        model = Article
        fields = {'content', 'title', 'author', }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }