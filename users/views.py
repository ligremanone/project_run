from typing import ClassVar

from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.serializers import UserDetailSerializer, UserSerializer


class UserPagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 50


class UsersTypeViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends: ClassVar[list[str]] = [
        SearchFilter,
        OrderingFilter,
    ]
    search_fields: ClassVar[list[str]] = [
        "last_name",
        "first_name",
    ]
    filterset_fields: ClassVar[list[str]] = [
        "date_joined",
    ]
    pagination_class = UserPagination

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset.filter(is_superuser=False)
        type = self.request.query_params.get("type", None)
        if type:
            if type == "coach":
                queryset = queryset.filter(is_staff=True)
            elif type == "athlete":
                queryset = queryset.filter(is_staff=False)
        return queryset

    def get_serializer_class(self) -> type[UserSerializer | UserDetailSerializer]:
        if self.action == "list":
            return UserSerializer
        if self.action == "retrieve":
            return UserDetailSerializer
        return super().get_serializer_class()
