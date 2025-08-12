from app_subscribe.models import Subscribe
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app_rating.models import Rating


class RatingAPIView(APIView):
    def post(self, request: Request, coach_id: int) -> Response:
        coach = get_object_or_404(
            User,
            id=coach_id,
        )
        rating = int(request.data.get("rating"))
        try:
            athlete = User.objects.get(id=request.data.get("athlete"))
        except User.DoesNotExist:
            return Response(
                {"message": "Athlete not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if rating < 1 or rating > 5:
            return Response(
                {"message": "Incorrect rating value"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if Subscribe.objects.filter(
            athlete=athlete,
            coach=coach,
        ).exists():
            if Rating.objects.filter(
                athlete=athlete,
                coach=coach,
            ).exists():
                Rating.objects.filter(
                    athlete=athlete,
                    coach=coach,
                ).update(
                    rating=rating,
                )
                return Response(
                    {"message": "Rating updated"},
                    status=status.HTTP_200_OK,
                )
            Rating.objects.create(
                athlete=athlete,
                coach=coach,
                rating=rating,
            )
            return Response(
                {"message": "Rating created"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Incorrect data"},
            status=status.HTTP_400_BAD_REQUEST,
        )
