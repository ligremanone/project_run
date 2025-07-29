from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_positions.views import PositionViewSet

router = DefaultRouter()
router.register(
    "",
    PositionViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
