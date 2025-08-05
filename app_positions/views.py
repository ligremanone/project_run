from app_run.models import Run
from collectible_items.models import CollectibleItem
from django.db.models import QuerySet
from project_run.settings.base import DISTANCE_TO_ITEM
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app_positions.models import Position
from app_positions.serializers import PositionSerializer
from app_positions.utils import is_distance_to_item_less_than


# Create your views here.
class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def create(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        response = super().create(request, *args, **kwargs)
        run_id = int(request.data["run"])
        run = Run.objects.get(id=run_id)
        items = CollectibleItem.objects.all()
        for item in items:
            if is_distance_to_item_less_than(
                request.data["latitude"],
                request.data["longitude"],
                float(item.latitude),
                float(item.longitude),
                DISTANCE_TO_ITEM,
            ):
                athlete = run.athlete
                athlete.collectible_items.add(item)
        return response

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        run_id = self.request.query_params.get("run", None)
        if run_id:
            return queryset.filter(run=run_id)
        return queryset
