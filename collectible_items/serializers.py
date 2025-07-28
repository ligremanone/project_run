from collectible_items.models import CollectibleItem
from rest_framework import serializers


class CollectibleItemSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source="picture")

    class Meta:
        model = CollectibleItem
        fields = [
            "name",
            "uid",
            "latitude",
            "longitude",
            "url",
            "value",
        ]

    def validate_latitude(self, value):
        if -90 <= value <= 90:
            return value
        raise serializers.ValidationError("Incorrect latitude value")

    def validate_longitude(self, value):
        if -180 <= value <= 180:
            return value
        raise serializers.ValidationError("Incorrect longitude value")
