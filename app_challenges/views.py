from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet

from app_challenges.models import Challenge
from app_challenges.serializers import ChallengeSerializer


# Create your views here.
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        athlete = self.request.query_params.get("athlete", None)
        if athlete:
            queryset = queryset.filter(athlete=int(athlete))
        return queryset
