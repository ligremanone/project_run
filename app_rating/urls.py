from django.urls import path

from app_rating.views import RatingAPIView

urlpatterns = [
    path(
        "",
        RatingAPIView.as_view(),
        name="rating",
    ),
]
