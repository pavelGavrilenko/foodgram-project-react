from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet, FavoriteApiView,
                    ShoppingListView, DownloadListIngredients, IngredientViewSet)

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)


urlpatterns = [
    path('recipes/download_shopping_cart/', DownloadListIngredients.as_view()),
    path('', include(router.urls)),
    path(
        'recipes/<int:favorite_id>/favorite/',
        FavoriteApiView.as_view()
    ),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        ShoppingListView.as_view()
    ),

]
