# Generated by Django 3.2 on 2022-12-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20221223_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steprecipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]