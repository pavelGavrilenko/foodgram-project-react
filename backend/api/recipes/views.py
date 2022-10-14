from rest_framework.permissions import AllowAny
from rest_framework import generics


from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = None


class IngredientRetrieve(generics.RetrieveAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [AllowAny, ]
