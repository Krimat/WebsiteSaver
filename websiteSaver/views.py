from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from .serializers import (SiteSerializer, TagSerializer)
from .models import (Site, Tag)
from .pagination import (SitePagination, TagPagination)
# Create your views here.


class SiteViewset(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    pagination_class = SitePagination

    permission_per_action = {
        "create": [permissions.IsAdminUser],
    }

    def get_queryset(self):
        queryset = Site.objects.all()

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__startswith=name)

        return queryset

    def get_permissions(self):
        permission_classes = []
        for action_type in self.permission_per_action:
            
            if self.action == action_type:
                permission_classes = self.permission_per_action[action_type]

        return (permission() for permission in permission_classes)

