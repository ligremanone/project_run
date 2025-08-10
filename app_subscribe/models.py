from typing import ClassVar

from django.contrib.auth.models import User
from django.db import models


class Subscribe(models.Model):
    athlete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="athlete_subscribe",
    )
    coach = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="coach_subscribe",
    )

    class Meta:
        constraints: ClassVar[list] = [
            models.UniqueConstraint(
                fields=["athlete", "coach"],
                name="unique_subscribe",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.athlete} - {self.coach}"
