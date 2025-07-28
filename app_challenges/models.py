from django.db import models

from app_athletes.models import AthleteInfo


class Challenge(models.Model):
    full_name = models.CharField(max_length=100)
    athlete = models.ForeignKey(
        AthleteInfo,
        on_delete=models.CASCADE,
    )
