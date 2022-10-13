from django.contrib.auth import get_user_model
from .serializers import CurrentUserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [AllowAny, ]
