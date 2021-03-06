from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    total_raised = models.IntegerField(default=0)
    num_suppoters = models.IntegerField(default=0)
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )


    
    