from django.forms import ModelForm
from django import  forms
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
        fields = ('stepRecipe', 'numIngredient', 'name', 'description')

        widgets = {
            'stepRecipe': forms.TextInput(attrs={'class': 'form-control'}),
            'numIngredient': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class IngredientForm(ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'
