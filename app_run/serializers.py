from app_athletes.serializers import AthleteSerializer
from rest_framework import serializers

from app_run.models import Run


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(
        read_only=True,
        source="athlete",
    )

    class Meta:
        model = Run
        fields = "__all__"
