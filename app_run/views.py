from pprint import pprint

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from app_run.models import Run
from app_positions.models import Position
from app_challenges.models import Challenge
from app_athletes.models import AthleteInfo
from app_run.serializers import (
    RunSerializer,
)
from collectible_items.models import CollectibleItem
from collectible_items.serializers import CollectibleItemSerializer
from project_run.settings.base import (
    COMPANY_NAME,
    SLOGAN,
    CONTACTS,
    CHALLENGE_DO_10_RUNS,
    CHALLENGE_50_KILOMETERS_RUNS,
)
from geopy import distance
from openpyxl import load_workbook


@api_view(["GET"])
def company_details(request: Request) -> Response:
    return Response(
        {
            "company_name": COMPANY_NAME,
            "slogan": SLOGAN,
            "contacts": CONTACTS,
        }
    )


@api_view(["POST"])
def upload_file(request):
    file = request.FILES.get("file")
    wb = load_workbook(file)
    sheet = wb.active
    headers = [
        "name",
        "uid",
        "value",
        "latitude",
        "longitude",
        "url",
    ]
    rows = list(sheet.iter_rows(values_only=True, min_row=2))
    error_data = []
    for idx, row in enumerate(rows, start=2):
        data = dict(zip(headers, row))
        serializer = CollectibleItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # collectible_item = CollectibleItem(**serializer.validated_data)
            # collectible_item.save()
        else:
            error_data.append(list(row))
    return Response(data=error_data)


class RunPagination(PageNumberPagination):
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
        run_distance = 0
        run = get_object_or_404(
            Run,
            id=run_id,
        )
        if run.status == Run.IN_PROGRESS:
            run.status = Run.FINISHED
            positions = Position.objects.filter(run=run)
            for i in range(len(positions) - 1):
                run_distance += distance.distance(
                    (positions[i].latitude, positions[i].longitude),
                    (positions[i + 1].latitude, positions[i + 1].longitude),
                ).km
            run.distance = round(run_distance, 3)
            run.save()
            finished_run_count = Run.objects.filter(
                status=Run.FINISHED, athlete=run.athlete.id
            ).count()
            if finished_run_count == 10:
                challenge = Challenge(
                    full_name=CHALLENGE_DO_10_RUNS,
                    athlete=AthleteInfo.objects.get(user_id=run.athlete),
                )
                challenge.save()
            total_distance = Run.objects.filter(athlete=run.athlete).aggregate(
                Sum("distance")
            )
            if total_distance.get("distance__sum") >= 50:
                challenge = Challenge(
                    full_name=CHALLENGE_50_KILOMETERS_RUNS,
                    athlete=AthleteInfo.objects.get(user_id=run.athlete),
                )
                challenge.save()
            return Response(
                {"message": "Run stopped"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Run not started or already finished"},
            status=status.HTTP_400_BAD_REQUEST,
        )
