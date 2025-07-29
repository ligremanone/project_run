from app_run.models import Run
from rest_framework import serializers

from app_positions.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

    def validate_run(self, value: Run) -> Run:
        if value.status == Run.IN_PROGRESS:
            return value
        raise serializers.ValidationError("Incorrect run status")

    def validate_latitude(self, value: int) -> int:
        if -90 <= value <= 90:
            return value
        raise serializers.ValidationError("Incorrect latitude value")

    def validate_longitude(self, value: int) -> int:
        if -180 <= value <= 180:
            return value
        raise serializers.ValidationError("Incorrect longitude value")
