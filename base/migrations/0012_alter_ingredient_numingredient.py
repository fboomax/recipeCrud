# Generated by Django 3.2 on 2022-12-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_ingredient_numingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='numIngredient',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]
