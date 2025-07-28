from django.urls import path

from app_athletes.views import AthleteInfoAPIView

urlpatterns = [
    path(
        "<int:athlete_id>/",
        AthleteInfoAPIView.as_view(),
        name="athlete_info",
    ),
]
