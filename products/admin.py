from django.contrib import admin
from .models import Product, Variety, Brand, Category, AvailabilitySize, VarietyImage


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the Product model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'name', 'brand', 'category', 'features')


class VarietyAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the Variety model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'color',)


class AvailabilitySizeAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the AvailabilitySize model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'size_type', 'price', 'count', 'discount')


class VarietyImageAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the VarietyImage model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'url')


class CategoryAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the Category model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'name')


class BrandAdmin(admin.ModelAdmin):
    """
    Class representing the admin interface for the Brand model.
    Specifies the fields to be displayed in the list view.
    """
    list_display = ('id', 'name')


# Register the models and their corresponding admin classes with the admin site.
admin.site.register(Product, ProductAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(AvailabilitySize, AvailabilitySizeAdmin)
admin.site.register(VarietyImage, VarietyImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
