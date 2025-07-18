from rest_framework import serializers

from app_run.models import Run
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


class RunSerializer(serializers.ModelSerializer):
    athlete_data = AthleteSerializer(
        read_only=True,
        source="athlete",
    )

    class Meta:
        model = Run
        fields = "__all__"
