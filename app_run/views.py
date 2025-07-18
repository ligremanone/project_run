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
from app_run.models import Run
from app_run.serializers import RunSerializer, UserSerializer
from project_run.settings.base import COMPANY_NAME, SLOGAN, CONTACTS


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
