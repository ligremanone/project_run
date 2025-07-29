from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app_athletes.models import AthleteInfo
from app_athletes.serializers import AthleteInfoSerializer


class AthleteInfoAPIView(APIView):
    def get(self, request: Request, athlete_id: int) -> Response:  # noqa: ARG002
        user = get_object_or_404(
            User,
            id=athlete_id,
        )
        athlete, created = AthleteInfo.objects.get_or_create(user_id=user)
        return Response(AthleteInfoSerializer(athlete).data)

    def put(self, request: Request, athlete_id: int) -> Response:
        if not request.data.get("weight").isdigit() or (
            int(request.data.get("weight")) <= 0
            or int(request.data.get("weight")) >= 900
        ):
            return Response(
                {"message": "Incorrect weight value"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = get_object_or_404(
            User,
            id=athlete_id,
        )
        athlete, created = AthleteInfo.objects.update_or_create(
            user_id=user,
            defaults={
                "weight": request.data.get("weight"),
                "goals": request.data.get("goals"),
            },
        )
        if created:
            return Response(
                {"message": "Athlete created"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Athlete info updated"},
            status=status.HTTP_200_OK,
        )
