from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import company_details, RunViewSet, UsersTypeViewSet

router = DefaultRouter()
router.register(
    "runs",
    RunViewSet,
)
router.register(
    "users",
    UsersTypeViewSet,
)
urlpatterns = [
    path("company_details/", company_details),
    path("", include(router.urls)),
]
