from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    product_name = models.CharField(max_length=255)

    expiry = models.CharField(max_length=100)

    preserve = models.TextField()

    ingredient = models.TextField()

    note = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', db_column='product_id')
    image_name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=500)
 
    class Meta:
        db_table = 'images'
 
    def __str__(self):
        return self.image_name
    
class ProductVariant(models.Model):
    variant_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', db_column='product_id')
    sku_code = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    fit = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
 
    class Meta:
        db_table = 'product_variant'
 
    def __str__(self):
        return f'{self.product.product_name} - {self.sku_code}'
    
