from rest_framework import serializers

from app_run.models import Run, AthleteInfo, Challenge, Position
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "date_joined",
            "username",
            "last_name",
            "first_name",
            "type",
            "runs_finished",
        ]

    def get_type(self, obj):
        return "coach" if obj.is_staff else "athlete"

    def get_runs_finished(self, obj):
        return obj.run_set.filter(status=Run.FINISHED).count()


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "last_name",
            "first_name",
        ]


class AthleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteInfo
        fields = "__all__"


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(
        read_only=True,
        source="athlete",
    )

    class Meta:
        model = Run
        fields = "__all__"


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

    def validate_run(self, value):
        if value.status == Run.IN_PROGRESS:
            return value
        raise serializers.ValidationError("Incorrect run status")

    def validate_latitude(self, value):
        if -90 <= value <= 90:
            return value
        raise serializers.ValidationError("Incorrect latitude value")

    def validate_longitude(self, value):
        if -180 <= value <= 180:
            return value
        raise serializers.ValidationError("Incorrect longitude value")


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = [
            "full_name",
            "athlete",
        ]
