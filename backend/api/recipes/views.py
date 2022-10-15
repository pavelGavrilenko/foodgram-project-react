from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets


from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer, RecipeFullSerializer
from .filters import RecipeFilter, IngredientFilter
from .permissions import IsAuthorOrReadOnly


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny, ]
    filter_class = IngredientFilter
    pagination_class = None


class IngredientRetrieve(generics.RetrieveAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny, ]


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly, ]
    queryset = Recipe.objects.all()
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return RecipeFullSerializer
        return RecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
