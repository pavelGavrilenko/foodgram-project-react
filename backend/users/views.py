from django.contrib.auth import get_user_model
from .serializers import CurrentUserSerializer
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import UserFollowSerializer, FollowListSerializer
from .models import CustomUser, Follow


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = [AllowAny, ]


class FollowApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, following_id):
        user = request.user
        data = {
            'following': following_id,
            'user': user.id
        }
        serializer = UserFollowSerializer(data=data,
                                          context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, following_id):
        user = request.user
        following = get_object_or_404(CustomUser, id=following_id)
        Follow.objects.filter(user=user, following=following).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = FollowListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(following__user=user)
