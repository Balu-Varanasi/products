from django.contrib import admin
from .models import Product, Property


class PropertiesInline(admin.StackedInline):
    model = Property
    extra = 4


class ProductAdmin(admin.ModelAdmin):
    inlines = [PropertiesInline, ]


admin.site.register(Product, ProductAdmin)
