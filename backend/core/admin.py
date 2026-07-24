from django.contrib import admin

from .models import SystemConfig


@admin.register(SystemConfig)
class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ("config_key", "config_value", "updated_at")
    search_fields = ("config_key", "config_value", "description")
    readonly_fields = ("updated_at",)
