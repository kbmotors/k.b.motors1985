from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = (
        'brand',
        'model_name',
        'year',
        'price',
        'fuel_type',
        'body_type',
        'transmission',
        'is_available',
    )

    list_filter = (
        'fuel_type',
        'body_type',
        'transmission',
        'is_available',
        'year',
    )

    search_fields = (
        'brand',
        'model_name',
    )

    ordering = (
        '-created_at',
    )