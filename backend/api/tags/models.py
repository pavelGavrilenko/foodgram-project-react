from django.db import models
from colorfield.fields import ColorField


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        verbose_name='Имя тега'
    )
    color = ColorField(
        default='#FF0000',
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг тэга'
    )

    def __str__(self):
        return self.name