from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.contrib.auth.models import User
from app_run.models import Run, AthleteInfo, Challenge
from app_run.serializers import (
    RunSerializer,
    UserSerializer,
    AthleteInfoSerializer,
    ChallengeSerializer,
)
from project_run.settings.base import (
    COMPANY_NAME,
    SLOGAN,
    CONTACTS,
    CHALLENGE_DO_10_RUNS,
)


@api_view(["GET"])
def company_details(request: Request) -> Response:
    return Response(
        {
            "company_name": COMPANY_NAME,
            "slogan": SLOGAN,
            "contacts": CONTACTS,
        }
    )


class RunPagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 50


class UserPagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 50


class RunViewSet(ModelViewSet):
    queryset = Run.objects.all().prefetch_related("athlete")
    serializer_class = RunSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = [
        "status",
        "athlete",
    ]
    ordering_fields = [
        "created_at",
    ]
    pagination_class = RunPagination


class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        queryset = self.queryset
        athlete = self.request.query_params.get("athlete", None)
        if athlete:
            queryset = queryset.filter(athlete=int(athlete))
        return queryset


class RunAPIStartView(APIView):
    def post(self, request: Request, run_id: int) -> Response:
        run = get_object_or_404(Run, id=run_id)
        if run.status == Run.INITIAL:
            run.status = Run.IN_PROGRESS
            run.save()
            return Response(
                {"message": "Run started"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Run already started or finished"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class RunAPIStopView(APIView):
    def post(self, request: Request, run_id: int) -> Response:
        run = get_object_or_404(
            Run,
            id=run_id,
        )
        if run.status == Run.IN_PROGRESS:
            run.status = Run.FINISHED
            run.save()
            return Response(
                {"message": "Run stopped"},
                status=status.HTTP_200_OK,
            )
        finished_run_count = Run.objects.filter(
            status=Run.FINISHED, athlete=run.athlete.id
        ).count()
        if finished_run_count == 10:
            challenge = Challenge(
                full_name=CHALLENGE_DO_10_RUNS,
                athlete=AthleteInfo.objects.get(user_id=run.athlete),
            )
            challenge.save()
        return Response(
            {"message": "Run not started or already finished"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UsersTypeViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = [
        "last_name",
        "first_name",
    ]
    filterset_fields = [
        "date_joined",
    ]
    pagination_class = UserPagination

    def get_queryset(self):
        queryset = self.queryset.filter(is_superuser=False)
        type = self.request.query_params.get("type", None)
        if type:
            if type == "coach":
                queryset = queryset.filter(is_staff=True)
            elif type == "athlete":
                queryset = queryset.filter(is_staff=False)
        return queryset


class AthleteInfoAPIView(APIView):
    def get(self, request: Request, athlete_id: int) -> Response:
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
