# Generated by Django 3.2 on 2022-12-20 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_steprecipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('stepRecipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.steprecipe')),
            ],
        ),
    ]
