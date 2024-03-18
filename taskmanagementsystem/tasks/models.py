from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 0, 'Baixa'
        MEDIUM = 1, 'Média'
        HIGH = 2, 'Alta'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
