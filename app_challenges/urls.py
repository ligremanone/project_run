from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_challenges.views import ChallengesSummaryViewSet, ChallengeViewSet

router = DefaultRouter()
router.register(
    "challenges",
    ChallengeViewSet,
    basename="challenges",
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "challenges_summary/",
        ChallengesSummaryViewSet.as_view(),
    ),
]
