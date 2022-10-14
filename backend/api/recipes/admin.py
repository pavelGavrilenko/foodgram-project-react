from django.contrib import admin
from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'unit'
    )
    search_fields = ('name',)


admin.site.register(Ingredient, IngredientAdmin)