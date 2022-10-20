from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet, FavoriteApiView,
                    ShoppingListView, DownloadListIngredients, IngredientViewSet)

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)


urlpatterns = [
    path('recipes/download_shopping_cart/', DownloadListIngredients.as_view(), name='download_shopping_cart'),
    path('', include(router.urls)),
    path(
        'recipes/<int:favorite_id>/favorite/',
        FavoriteApiView.as_view(),
        name='favorite'
    ),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        ShoppingListView.as_view(),
        name='shopping_cart'
    ),

]
