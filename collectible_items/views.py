from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from collectible_items.models import CollectibleItem
from collectible_items.serializers import (
    CollectibleItemSerializer,
    CollectibleItemListSerializer,
)


class CollectibleItemViewSet(ModelViewSet):
    queryset = CollectibleItem.objects.all()
    serializer_class = CollectibleItemListSerializer
