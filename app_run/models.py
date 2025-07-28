from django.db import models
from django.contrib.auth.models import User


class Run(models.Model):
    INITIAL = "init"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    STATUS_CHOICES = [
        (INITIAL, "Initial"),
        (IN_PROGRESS, "In progress"),
        (FINISHED, "Finished"),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=INITIAL,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    athlete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        blank=True,
        null=True,
    )
    distance = models.FloatField(
        blank=True,
        null=True,
    )
