from django.urls import path

from app_run.views import base_view

urlpatterns = [
    path("company_details/", base_view),
]
