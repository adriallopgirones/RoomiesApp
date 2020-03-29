from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    group_id = models.TextField(max_length=100, blank=True)
    is_grouped = models.BooleanField(default=False)
    debt = models.FloatField(default=0)