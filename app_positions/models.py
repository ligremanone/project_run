from app_run.models import Run
from django.db import models


class Position(models.Model):
    run = models.ForeignKey(
        Run,
        on_delete=models.CASCADE,
    )
    latitude = models.DecimalField(
        max_digits=6,
        decimal_places=4,
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
    )
    date_time = models.DateTimeField(
        blank=True,
        null=True,
    )
    speed = models.FloatField(
        blank=True,
        default=0.0,
    )
    distance = models.FloatField(
        blank=True,
        default=0.0,
    )

    def __str__(self) -> str:
        return f"{self.run} {self.date_time}"
