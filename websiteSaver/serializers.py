from rest_framework import serializers

from .models import (Site, Tag)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'description', 'added', 'image']
        model = Site
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        field = ['name']
        model = Tag