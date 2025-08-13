from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_run.views import (
    CoachAnalyticsView,
    RunAPIStartView,
    RunAPIStopView,
    RunViewSet,
    company_details,
    upload_file,
)

router = DefaultRouter()
router.register(
    "runs",
    RunViewSet,
)
urlpatterns = [
    path("company_details/", company_details),
    path("upload_file/", upload_file),
    path("", include(router.urls)),
    path("runs/<int:run_id>/start/", RunAPIStartView.as_view(), name="start_run"),
    path("runs/<int:run_id>/stop/", RunAPIStopView.as_view(), name="stop_run"),
    path(
        "analytics_for_coach/<int:coach_id>/",
        CoachAnalyticsView.as_view(),
        name="coach_analytics",
    ),
]
