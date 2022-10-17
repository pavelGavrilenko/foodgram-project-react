from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (IngredientList, IngredientRetrieve, RecipeViewSet,
                    FavoriteApiView, ShoppingListView, DownloadListIngredients)

router = DefaultRouter()
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('recipes/download_shopping_cart/', DownloadListIngredients.as_view()),
    path('ingredients/', IngredientList.as_view()),
    path('ingredients/<int:pk>/', IngredientRetrieve.as_view()),
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
