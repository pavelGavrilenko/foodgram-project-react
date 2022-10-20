from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

from tags.models import Tag


User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        verbose_name='Название продукта'
    )
    measurement_unit = models.CharField(
        max_length=15,
        null=False,
        verbose_name='Единицы измерения'
    )

    def __str__(self):
        return f'Ингредиент {self.name}'


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        related_name='ingredients_in_recipe', verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE,
        related_name='recipes_ingredients_list', verbose_name='Рецепт'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество ингредиента'
    )

    class Meta:
        verbose_name = 'Количество'
        constraints = [
            UniqueConstraint(fields=['recipe', 'ingredient'], name='ingredient_recipe')
        ]

    def __str__(self):
        return f'Количество {self.ingredient} в {self.recipe}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        through='IngredientAmount',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэг'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField(
        verbose_name='Описание',
        max_length=3000
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название рецепта',
        null=False
    )
    image = models.ImageField(
        upload_to='media/',
        verbose_name='Изображение'
    )
    cooking_time = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1, 'Значение не может быть меньше 1')],
        verbose_name='Время готовки в минутах',
    )

    class Meta:
        verbose_name = 'Рецепт'
        ordering = ['-pub_date']

    def __str__(self):
        return f'Рецепт {self.name}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        related_name='favorites',
        on_delete=models.CASCADE,
        verbose_name='Пользоавтель избранного'
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='favorites',
        on_delete=models.CASCADE,
        verbose_name='Рецепт в избранном'
    )

    class Meta:
        verbose_name = 'Избранные рецепты'
        constraints = [
            UniqueConstraint(fields=['recipe', 'user'], name='favorite_unique')
        ]


    def __str__(self):
        return f"{self.user} добавил в избранное {self.recipe}"


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_shopping_list',
        verbose_name='Пользоавтель листа покупок'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='Рецепт в покупках'
    )

    class Meta:
        verbose_name = 'Лист покупок'
        constraints = [
            UniqueConstraint(fields=['recipe', 'user'], name='list_unique')
        ]

    def __str__(self):
        return f'Пользователь {self.user} добавил в покупки {self.recipe}'


