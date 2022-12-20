from django.contrib import admin
from .models import Recipe, StepRecipe, Ingredient

admin.site.register(Recipe)
admin.site.register(StepRecipe)
admin.site.register(Ingredient)

