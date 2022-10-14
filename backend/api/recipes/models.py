from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Название продукта'
    )
    unit = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Единицы измерения'
    )

    def __str__(self):
        return f'Ингредиент {self.name}'


