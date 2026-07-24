from django.contrib import admin

from .models import Order, OrderDetail, OrderItem, PaymentTransaction


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "user", "total_amount", "payment_status", "order_status", "order_date")
    list_filter = ("payment_status", "order_status", "delivery_method", "payment_timing")
    search_fields = ("order_id", "user__username", "user__phone")
    readonly_fields = ("order_date", "updated_at")


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("order_detail_id", "order", "variant", "quantity", "unit_price")
    search_fields = ("order__order_id", "variant__sku_code")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order_item_id", "order_detail", "position", "custom_message")
    search_fields = ("custom_message",)


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "order", "transaction_type", "amount", "status", "created_at")
    list_filter = ("transaction_type", "status")
    search_fields = ("transaction_id", "order__order_id", "vnpay_transaction_id")
    readonly_fields = ("created_at",)
