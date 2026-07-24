from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Address, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "is_staff", "is_active")
    search_fields = ("username", "email", "phone")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("phone",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": ("phone",)}),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "city", "nation", "is_default", "user")
    list_filter = ("is_default", "city", "nation")
    search_fields = ("full_name", "phone", "home_address", "user__username")
