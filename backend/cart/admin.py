from django.contrib import admin

from .models import Cart, CartDetail, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_id", "user")
    search_fields = ("user__username", "user__phone")


@admin.register(CartDetail)
class CartDetailAdmin(admin.ModelAdmin):
    list_display = ("cart_detail_id", "cart", "variant", "quantity")
    search_fields = ("cart__user__username", "variant__sku_code")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart_item_id", "cart_detail", "position", "custom_message")
    search_fields = ("custom_message",)
