from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    user = models.TextField()
    date = models.DateField()
    task_name = models.TextField()
    description = models.TextField()