from typing import ClassVar

from app_run.models import Run
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    runs_finished = serializers.SerializerMethodField()

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

    def get_runs_finished(self, obj: User) -> int:
        return obj.run_set.filter(status=Run.FINISHED).count()
