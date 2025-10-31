# timesheet/forms.py
from django import forms
from . import models

class createform(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = ['project', 'module', 'task', 'date', 'time', 'description']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'module': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.25'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(createform, self).__init__(*args, **kwargs)
    #     self.fields['module'].queryset = models.Module.objects.none()
    #     self.fields['task'].queryset = models.Task.objects.none()

    #     if 'project' in self.data:
    #         try:
    #             project_id = int(self.data.get('project'))
    #             self.fields['module'].queryset = models.Module.objects.filter(project_id=project_id)
    #         except (ValueError, TypeError):
    #             pass

    #     if 'module' in self.data:
    #         try:
    #             module_id = int(self.data.get('module'))
    #             self.fields['task'].queryset = models.Task.objects.filter(module_id=module_id)
    #         except (ValueError, TypeError):
    #             pass
