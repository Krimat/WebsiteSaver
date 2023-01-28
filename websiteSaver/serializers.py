from rest_framework import serializers

from .models import (Site, Tag)
from .pagination import (SitePagination)

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'description', 'added', 'image']
        model = Site
        pagination_class = SitePagination

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        field = ['name']
        model = Tag