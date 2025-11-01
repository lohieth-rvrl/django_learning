from django.db import models
from django.contrib.auth.models import User

class todos(models.Model):
    choices = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    status = [('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=choices, default='Medium')
    status = models.CharField(max_length=20, choices=status, default='In Progress')

    def __str__(self):
        return self.title
