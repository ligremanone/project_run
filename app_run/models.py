from typing import ClassVar

from django.contrib.auth.models import User
from django.db import models


class Run(models.Model):
    INITIAL = "init"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"
    STATUS_CHOICES: ClassVar[list] = [
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
        default="",
    )
    distance = models.FloatField(
        blank=True,
        null=True,
    )
    run_time_seconds = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.pk} - {self.athlete.username} - {self.status}"
