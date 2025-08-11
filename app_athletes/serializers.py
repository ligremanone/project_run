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


class AthleteInfoForChallengeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = AthleteInfo
        fields: ClassVar[list] = [
            "id",
            "full_name",
            "username",
        ]

    def get_id(self, obj: AthleteInfo) -> int:
        return obj.user_id_id

    def get_full_name(self, obj: AthleteInfo) -> str:
        return f"{obj.user_id.first_name} {obj.user_id.last_name}"

    def get_username(self, obj: AthleteInfo) -> str:
        return obj.user_id.username
