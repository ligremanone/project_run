from typing import ClassVar

from collectible_items.serializers import CollectibleItemListSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.IntegerField()

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
