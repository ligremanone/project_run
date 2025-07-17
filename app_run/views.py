from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from project_run.settings.base import COMPANY_NAME, SLOGAN, CONTACTS


@api_view(["GET"])
def base_view(request: Request) -> Response:
    return Response(
        {
            "company_name": COMPANY_NAME,
            "slogan": SLOGAN,
            "contacts": CONTACTS,
        }
    )
