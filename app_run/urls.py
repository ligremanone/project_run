from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import (
    company_details,
    RunViewSet,
    UsersTypeViewSet,
    RunAPIStartView,
    RunAPIStopView,
    AthleteInfoAPIView,
    ChallengeViewSet,
    PositionViewSet,
)

router = DefaultRouter()
router.register(
    "runs",
    RunViewSet,
)
router.register(
    "users",
    UsersTypeViewSet,
)
router.register(
    "challenges",
    ChallengeViewSet,
)
router.register(
    "positions",
    PositionViewSet,
)
urlpatterns = [
    path("company_details/", company_details),
    path("", include(router.urls)),
    path("runs/<int:run_id>/start/", RunAPIStartView.as_view(), name="start_run"),
    path("runs/<int:run_id>/stop/", RunAPIStopView.as_view(), name="stop_run"),
    path(
        "athlete_info/<int:athlete_id>/",
        AthleteInfoAPIView.as_view(),
        name="athlete_info",
    ),
]
