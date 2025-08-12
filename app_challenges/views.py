from collections import defaultdict

from app_athletes.serializers import AthleteInfoForChallengeSerializer
from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app_challenges.models import Challenge
from app_challenges.serializers import ChallengeSerializer


class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        athlete = self.request.query_params.get("athlete", None)
        if athlete:
            queryset = queryset.filter(athlete=int(athlete))
        return queryset


class ChallengesSummaryViewSet(APIView):
    def get(
        self,
        request: Request,  # noqa: ARG002
        *args: set,  # noqa: ARG002
        **kwargs: dict,  # noqa: ARG002
    ) -> Response:
        challenges = Challenge.objects.select_related("athlete__user_id").order_by(
            "full_name",
        )
        grouped = defaultdict(list)
        for challenge in challenges:
            grouped[challenge.full_name].append(challenge.athlete)
        data = [
            {
                "name_to_display": name,
                "athletes": AthleteInfoForChallengeSerializer(athletes, many=True).data,
            }
            for name, athletes in grouped.items()
        ]
        return Response(data)
