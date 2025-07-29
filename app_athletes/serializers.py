from typing import ClassVar

from django.contrib.auth.models import User
from rest_framework import serializers

from app_athletes.models import AthleteInfo


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: ClassVar[list] = [
            "id",
            "username",
            "last_name",
            "first_name",
        ]


class AthleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteInfo
        fields = "__all__"
