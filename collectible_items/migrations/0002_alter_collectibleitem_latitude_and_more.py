# Generated by Django 5.2 on 2025-07-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [  # noqa: RUF012
        ("collectible_items", "0001_initial"),
    ]

    operations = [  # noqa: RUF012
        migrations.AlterField(
            model_name="collectibleitem",
            name="latitude",
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name="collectibleitem",
            name="longitude",
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
    ]
