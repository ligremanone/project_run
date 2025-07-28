from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.serializers import UserSerializer


class UserPagination(PageNumberPagination):
    page_size_query_param = "size"
    max_page_size = 50


class UsersTypeViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]
    search_fields = [
        "last_name",
        "first_name",
    ]
    filterset_fields = [
        "date_joined",
    ]
    pagination_class = UserPagination

    def get_queryset(self):
        queryset = self.queryset.filter(is_superuser=False)
        type = self.request.query_params.get("type", None)
        if type:
            if type == "coach":
                queryset = queryset.filter(is_staff=True)
            elif type == "athlete":
                queryset = queryset.filter(is_staff=False)
        return queryset
