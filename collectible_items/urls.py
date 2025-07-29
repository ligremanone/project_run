from django.urls import include, path
from rest_framework.routers import DefaultRouter

from collectible_items.views import CollectibleItemViewSet

router = DefaultRouter()
router.register(
    "",
    CollectibleItemViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
]
