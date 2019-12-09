from django.contrib import admin

# Register your models here.

from .models import Product, Category, Property, Measurement, ProductImage

admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Measurement)
admin.site.register(ProductImage)


class PropertiesInline(admin.TabularInline):
    model = Property
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'price', 'quantity', 'productCode', 'categories']}),
    ]
    inlines = [PropertiesInline]
    list_display = ('id', 'title')


admin.site.register(Product, ProductAdmin)

