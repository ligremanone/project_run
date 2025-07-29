from app_athletes.models import AthleteInfo
from django.db import models


class Challenge(models.Model):
    full_name = models.CharField(max_length=100)
    athlete = models.ForeignKey(
        AthleteInfo,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.full_name
