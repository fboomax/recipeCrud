from django.forms import ModelForm
from .models import Recipe, StepRecipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class StepRecipeForm(ModelForm):
    class Meta:
        model = StepRecipe
        fields = '__all__'


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
