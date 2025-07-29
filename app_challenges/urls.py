from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_challenges.views import ChallengeViewSet

router = DefaultRouter()
router.register(
    "",
    ChallengeViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
