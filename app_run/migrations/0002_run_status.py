# Generated by Django 5.2 on 2025-07-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [  # noqa: RUF012
        ("app_run", "0001_initial"),
    ]

    operations = [  # noqa: RUF012
        migrations.AddField(
            model_name="run",
            name="status",
            field=models.CharField(
                choices=[
                    ("init", "Initial"),
                    ("in_progress", "In progress"),
                    ("finished", "Finished"),
                ],
                default="init",
                max_length=20,
            ),
        ),
    ]
