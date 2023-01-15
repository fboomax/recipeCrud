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
    image = models.ImageField(upload_to='media')
    # serialId = models.AutoField(primary_key=False)
    # serialId = models.Se(
    #     primary_key=False,
    #     editable=False,
    #     help_text=("Auto Increment Number"),
    #     verbose_name=("Number"),
    #     # null=True
    # )
    # serialId = models.UUIDField(
    #     primary_key=False,
    #     null=True,
    #     editable=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.name


class StepRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.IntegerField()
    title = models.CharField(max_length=80)
    description = models.TextField()
    # ingredient
    duration = models.FloatField(validators=[MinValueValidator(0.0)])
    image = models.ImageField(upload_to='media', null=True, blank=True)
    # progressBar

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recipe.Id:{self.recipe.id} Step.Id{self.id} - {self.recipe} :Step_num:{self.step} {self.title}'


class Ingredient(models.Model):
    stepRecipe = models.ForeignKey(StepRecipe, on_delete=models.CASCADE)
    # numIngredient = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return f'{self.stepRecipe} : {self.name}'
