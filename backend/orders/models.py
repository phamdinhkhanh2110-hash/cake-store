from django.db import models

from accounts.models import Address
from django.conf import settings

from catalog.models import ProductVariant

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='orders', db_column='user_id')
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='staff_orders', db_column='staff_id', blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='orders', db_column='address_id')
    delivery_method = models.CharField(max_length=50)
    payment_timing = models.CharField(max_length=50)
    deposit_percentage = models.PositiveIntegerField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    shipping_fee = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    requested_time = models.DateTimeField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    cancelled_by = models.CharField(max_length=100, blank=True, null=True)
    cancel_reason = models.TextField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'order'
 
    def __str__(self):
        return f'Order #{self.order_id}'

class OrderDetail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details', db_column='order_id')
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name='order_details', db_column='variant_id')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
 
    class Meta:
        db_table = 'order_detail'
 
    def __str__(self):
        return f'OrderDetail #{self.order_detail_id}'

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, related_name='items', db_column='order_detail_id')
    position = models.PositiveIntegerField()
    custom_message = models.CharField(max_length=500, blank=True, null=True)
 
    class Meta:
        db_table = 'order_item'
 
    def __str__(self):
        return f'OrderItem #{self.order_item_id}'

class PaymentTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions', db_column='order_id')
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    vnpay_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    refund_bank_account = models.CharField(max_length=255, blank=True, null=True)
    refund_proof_image = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = 'payment_transaction'
 
    def __str__(self):
        return f'Transaction #{self.transaction_id}'