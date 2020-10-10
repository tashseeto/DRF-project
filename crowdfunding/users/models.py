from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.URLField(default="")
    date_joined = models.DateTimeField(default=timezone.now)
    project_owner = models.BooleanField(default=True)

    def __str__(self):
        return self.username



