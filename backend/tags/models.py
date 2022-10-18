from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        verbose_name='Имя тега'
    )
    color = models.CharField(
        max_length=16,
        default='#FF0000',
        unique=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Слаг тэга'
    )

    def __str__(self):
        return self.name