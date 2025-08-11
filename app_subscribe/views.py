from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app_subscribe.models import Subscribe


class SubscribeAPIView(APIView):
    def post(self, request: Request, id: int) -> Response:
        coach = get_object_or_404(
            User,
            id=id,
        )
        try:
            athlete = User.objects.get(id=request.data.get("athlete"))
        except User.DoesNotExist:
            return Response(
                {"message": "Athlete not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if Subscribe.objects.filter(coach=coach, athlete=athlete).exists():
            return Response(
                {"message": "Subscribe already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if coach and athlete and coach.is_staff and not athlete.is_staff:
            subscribe = Subscribe(coach=coach, athlete=athlete)
            subscribe.save()
            return Response(
                {"message": "Subscribe created"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Incorrect data"},
            status=status.HTTP_400_BAD_REQUEST,
        )
