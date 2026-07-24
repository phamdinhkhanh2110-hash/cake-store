from django.db import models
from django.conf import settings
from catalog.models import ProductVariant
# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', db_column='user_id')
 
    class Meta:
        db_table = 'cart'
 
    def __str__(self):
        return f"Cart #{self.cart_id} - {self.user.username}"

class CartDetail(models.Model):
    cart_detail_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='details', db_column='cart_id')
    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name='cart_details', db_column='variant_id')
    quantity = models.PositiveIntegerField(default=1)
 
    class Meta:
        db_table = 'cart_detail'
 
    def __str__(self):
        return f'CartDetail #{self.cart_detail_id}'
    
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart_detail = models.ForeignKey(CartDetail, on_delete=models.CASCADE, related_name='items', db_column='cart_detail_id')
    position = models.PositiveIntegerField()
    custom_message = models.CharField(max_length=500, blank=True, null=True)
 
    class Meta:
        db_table = 'cart_item'
 
    def __str__(self):
        return f'CartItem #{self.cart_item_id}'