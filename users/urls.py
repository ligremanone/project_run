from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import UsersTypeViewSet

router = DefaultRouter()
router.register(
    "",
    UsersTypeViewSet,
)
urlpatterns = [
    path("", include(router.urls)),
]
