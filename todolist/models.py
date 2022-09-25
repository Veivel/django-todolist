from time import timezone
from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date = models.DateField()
    task_name = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)