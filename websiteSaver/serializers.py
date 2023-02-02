from rest_framework import serializers

from .models import (Site, Tag)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Site
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Tag