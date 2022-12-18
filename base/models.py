from django.db import models
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=40)
    DIFFICULTY = (
        ('EASY', 'easy'),
        ('MODERATE', 'moderate'),
        ('HARD', 'hard')
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    steps = models.PositiveIntegerField(null=True)
    duration = models.FloatField(validators=[MinValueValidator(0.0)])
    photo = models.ImageField(upload_to='media')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
