from django.contrib import admin

from .models import Category, Images, Product, ProductVariant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category_name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "category", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("product_name",)


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("image_name", "product")
    search_fields = ("image_name", "product__product_name")


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("sku_code", "product", "size", "price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("sku_code", "product__product_name")
