from django.contrib import admin

# Register your models here.

from .models import Product, Category, Property, Measurement, ProductImage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Measurement)
admin.site.register(ProductImage)