# Generated by Django 3.2 on 2023-01-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_ingredient_numingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='numIngredient',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
