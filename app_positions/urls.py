from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app_positions.views import PositionViewSet

router = DefaultRouter()
router.register(
    "",
    PositionViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
