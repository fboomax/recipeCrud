from django.forms import ModelForm
from django import forms
from .models import Recipe, StepRecipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class StepRecipeForm(ModelForm):
    class Meta:
        model = StepRecipe
        fields = '__all__'

        # widgets = {
        #     # 'recipe': forms.TextInput(attrs={'class': 'form-control'}),
        #     'step': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'duration': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'image': forms.ImageField(),
        # }

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ( 'name', 'description')

        widgets = {
            # 'stepRecipe': forms.TextInput(attrs={'class': 'form-control'}),
            # 'numIngredient': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class IngredientForm(ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'
