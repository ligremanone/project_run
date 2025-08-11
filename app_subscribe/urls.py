from django.urls import path

from app_subscribe.views import SubscribeAPIView

urlpatterns = [
    path(
        "",
        SubscribeAPIView.as_view(),
        name="subscribe",
    ),
]
