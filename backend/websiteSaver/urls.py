from rest_framework import routers
from django.urls import path, include


from .views import (SiteViewset)

router = routers.DefaultRouter()
router.register('sites', SiteViewset)

urlpatterns = [
    path('', include(router.urls)),
]