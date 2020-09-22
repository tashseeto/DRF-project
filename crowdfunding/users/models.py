from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.URLField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.username



