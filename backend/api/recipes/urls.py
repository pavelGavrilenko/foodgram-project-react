from django.urls import include, path

from .views import IngredientList, IngredientRetrieve


urlpatterns = [
    path('ingredients/', IngredientList.as_view()),
    path('ingredients/<int:pk>/', IngredientRetrieve.as_view()),
]