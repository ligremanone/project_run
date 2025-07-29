from rest_framework.viewsets import ModelViewSet

from app_positions.models import Position
from app_positions.serializers import PositionSerializer


# Create your views here.
class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
