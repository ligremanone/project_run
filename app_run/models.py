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


class AthleteInfo(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    goals = models.TextField(
        max_length=50,
        blank=True,
        null=True,
    )
    weight = models.IntegerField(
        blank=True,
        null=True,
    )


class Challenge(models.Model):
    full_name = models.CharField(max_length=100)
    athlete = models.ForeignKey(
        AthleteInfo,
        on_delete=models.CASCADE,
    )


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
