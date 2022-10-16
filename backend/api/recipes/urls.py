from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientList, IngredientRetrieve,RecipeViewSet, FavoriteApiView

router = DefaultRouter()
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('ingredients/', IngredientList.as_view()),
    path('ingredients/<int:pk>/', IngredientRetrieve.as_view()),
    path('', include(router.urls)),
    path(
        'recipes/<int:favorite_id>/favorite/',
        FavoriteApiView.as_view()
    ),
]
