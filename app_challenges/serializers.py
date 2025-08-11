from typing import ClassVar

from app_athletes.serializers import (
    AthleteInfoForChallengeSerializer,
)
from rest_framework import serializers

from app_challenges.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields: ClassVar[list] = [
            "full_name",
            "athlete",
        ]


class ChallengesSummarySerializer(serializers.ModelSerializer):
    name_to_display = serializers.CharField(
        source="full_name",
        read_only=True,
    )
    athletes = AthleteInfoForChallengeSerializer(
        read_only=True,
        source="athlete",
    )

    class Meta:
        model = Challenge
        fields: ClassVar[list] = [
            "name_to_display",
            "athletes",
        ]
