from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app_run.models import Run
from app_run.serializers import RunSerializer
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


class RunViewSet(ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
