from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint



class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        verbose_name='Никнейм'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль'
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        max_length=254
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'

    def __str__(self):
        return f'Юзер {self.username}'


User = get_user_model()


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписка',
        related_name='following'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower'
    )

    class Meta:
        verbose_name = 'Подписки'
        UniqueConstraint(
            fields=['following', 'user'],
            name='follow_unique'
        )

    def __str__(self):
        return f"Пользователь {self.user} подписан на {self.following}"
