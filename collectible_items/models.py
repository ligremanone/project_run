from django.db import models


class CollectibleItem(models.Model):
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    latitude = models.DecimalField(
        max_digits=6,
        decimal_places=4,
    )
    longitude = models.DecimalField(
        max_digits=7,
        decimal_places=4,
    )
    picture = models.URLField()
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.name
