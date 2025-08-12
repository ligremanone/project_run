from typing import ClassVar

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    athlete = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="athlete_rating",
    )
    coach = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="coach_rating",
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    class Meta:
        constraints: ClassVar[list] = [
            models.UniqueConstraint(
                fields=["athlete", "coach"],
                name="unique_rating",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.athlete} - {self.coach} - {self.rating}"
