from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app_challenges.views import ChallengeViewSet

router = DefaultRouter()
router.register(
    "",
    ChallengeViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
