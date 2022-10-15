from rest_framework.permissions import AllowAny
from rest_framework import generics

from .models import Tag
from .serializers import TagSerializer


class TagList(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = None


class TagRetrieve(generics.RetrieveAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [AllowAny, ]




