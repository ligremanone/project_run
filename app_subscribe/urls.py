from django.urls import path

from app_subscribe.views import SubscribeAPIView

urlpatterns = [
    path(
        "<int:coach_id>",
        SubscribeAPIView.as_view(),
        name="subscribe",
    ),
]
