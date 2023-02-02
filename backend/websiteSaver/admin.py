from django.contrib import admin


from .models import (Site, Tag)
# Register your models here.

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    exclude = ()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ()




