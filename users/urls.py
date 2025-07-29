from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UsersTypeViewSet

router = DefaultRouter()
router.register(
    "",
    UsersTypeViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
