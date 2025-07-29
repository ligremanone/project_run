from typing import ClassVar

from rest_framework import serializers

from collectible_items.models import CollectibleItem


class CollectibleItemSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source="picture")

    class Meta:
        model = CollectibleItem
        fields: ClassVar[list[str]] = [
            "name",
            "uid",
            "latitude",
            "longitude",
            "url",
            "value",
        ]

    def validate_latitude(self, value: int) -> int:
        if -90 <= value <= 90:
            return value
        raise serializers.ValidationError("Incorrect latitude value")

    def validate_longitude(self, value: int) -> int:
        if -180 <= value <= 180:
            return value
        raise serializers.ValidationError("Incorrect longitude value")


class CollectibleItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectibleItem
        fields = "__all__"
