from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import (
    company_details,
    RunViewSet,
    RunAPIStartView,
    RunAPIStopView,
)

router = DefaultRouter()
router.register(
    "",
    RunViewSet,
)
urlpatterns = [
    path("company_details/", company_details),
    path("", include(router.urls)),
    path("runs/<int:run_id>/start/", RunAPIStartView.as_view(), name="start_run"),
    path("runs/<int:run_id>/stop/", RunAPIStopView.as_view(), name="stop_run"),
]
