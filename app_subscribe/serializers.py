from typing import ClassVar

from rest_framework import serializers

from app_subscribe.models import Subscribe


class SubscribeSerializer(serializers.Serializer):
    class Meta:
        model = Subscribe
        fields = "__all__"
        validators: ClassVar[list] = [
            serializers.UniqueTogetherValidator(
                queryset=Subscribe.objects.all(),
                fields=["athlete", "coach"],
                message="Subscribe already exists",
            ),
        ]
