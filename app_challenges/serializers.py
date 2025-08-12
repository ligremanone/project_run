from typing import ClassVar

from rest_framework import serializers

from app_challenges.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields: ClassVar[list] = [
            "full_name",
            "athlete",
        ]
