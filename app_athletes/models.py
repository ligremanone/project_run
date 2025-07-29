from django.contrib.auth.models import User
from django.db import models


class AthleteInfo(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    goals = models.TextField(
        max_length=50,
        blank=True,
        default="",
    )
    weight = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.user_id}"
