from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import company_details, RunViewSet

router = DefaultRouter()
router.register(
    "runs",
    RunViewSet,
)
urlpatterns = [
    path("company_details/", company_details),
    path("", include(router.urls)),
]
