# Generated by Django 3.2.16 on 2022-10-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('unit', models.CharField(max_length=50, verbose_name='Единицы измерения')),
            ],
        ),
    ]
