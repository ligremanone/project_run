from rest_framework.viewsets import ModelViewSet

from collectible_items.models import CollectibleItem
from collectible_items.serializers import (
    CollectibleItemListSerializer,
)


class CollectibleItemViewSet(ModelViewSet):
    queryset = CollectibleItem.objects.all()
    serializer_class = CollectibleItemListSerializer
