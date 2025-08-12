from typing import ClassVar

from app_subscribe.models import Subscribe
from collectible_items.serializers import CollectibleItemListSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.IntegerField()
    rating = serializers.FloatField()

    class Meta:
        model = User
        fields: ClassVar[list[str]] = [
            "id",
            "date_joined",
            "username",
            "last_name",
            "first_name",
            "type",
            "runs_finished",
            "rating",
        ]

    def get_type(self, obj: User) -> str:
        return "coach" if obj.is_staff else "athlete"


class UserDetailSerializer(UserSerializer):
    items = CollectibleItemListSerializer(
        read_only=True,
        source="collectible_items",
        many=True,
    )

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + [
            "items",
        ]


class AthleteUserDetailSerializer(UserDetailSerializer):
    coach = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + [
            "coach",
        ]

    def get_coach(self, obj: User) -> int | None:
        if Subscribe.objects.filter(athlete=obj).exists():
            return Subscribe.objects.filter(athlete=obj).first().coach.id
        return None


class CoachUserDetailSerializer(UserDetailSerializer):
    athletes = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + [
            "athletes",
        ]

    def get_athletes(self, obj: User) -> list[int]:
        return [
            subscribe.athlete.id for subscribe in Subscribe.objects.filter(coach=obj)
        ]
