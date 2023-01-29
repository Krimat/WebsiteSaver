from django.shortcuts import render
from rest_framework import viewsets


from .serializers import (SiteSerializer, TagSerializer)
from .models import (Site, Tag)
from .pagination import (SitePagination)
# Create your views here.


class SiteViewset(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    pagination_class = SitePagination
    
    
    def get_queryset(self):
        queryset = Site.objects.all()


        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__startswith=name)
        return queryset



