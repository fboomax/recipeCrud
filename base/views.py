from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, StepRecipe, Ingredient
from .forms import RecipeForm, StepRecipeForm, IngredientForm
from django.core.paginator import Paginator
from django.views import View
from django.urls import reverse
from django.views.generic import FormView


class HomeView(View):
    def get(self, request):
        return render(request, 'base/home.html')


class RecipeListView(View):
    def get(self, request):
        allRecipes = Recipe.objects.all()
        context = {'allRecipes': allRecipes}
        return render(request, 'base/recipes.html', context)


class CreateRecipeView(View):
    def get(self, request):
        form = RecipeForm()
        context = {'form': form}
        return render(request, 'base/recipe_form.html', context)

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            obj = Recipe.objects.create(**data)
            print(obj)
            obj.save()
            return redirect('recipes')
        else:
            context = {'form': form}
            return render(request, 'base/recipe_form.html', context)


class RecipeView(View):
    def get(self, request, recipe_pk):
        selectedRecipe = Recipe.objects.get(id=recipe_pk)
        context = {'selectedRecipe': selectedRecipe}
        return render(request, 'base/recipe.html', context)


class UpdateRecipeView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        form = RecipeForm(instance=recipe)
        context = {'form': form}
        return render(request, 'base/recipe_form.html', context)

    def post(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')


class DeleteRecipeView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        return render(request, 'base/delete.html', {'obj': recipe})

    def post(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        recipe.delete()
        return redirect('recipes')


class StepRecipeListView(View):

    def get(self, request, recipe_pk):
        page = request.GET.get('page', 1)
        recipe = Recipe.objects.get(id=int(recipe_pk))
        stepsRecipe = recipe.steprecipe_set.order_by('step')
        paginator = Paginator(stepsRecipe, per_page=1)
        page_object = paginator.get_page(page)

        context = {"page_obj": page_object, "recipe_id": recipe_pk}
        return render(request, "base/steplist.html", context)


class IngredientListView(View):

    def get(self, request, recipe_pk, step_num):

        recipe = Recipe.objects.get(id=int(recipe_pk))
        stepRecipe = recipe.steprecipe_set.get(id=step_num)
        ingredients = Ingredient.objects.filter(stepRecipe__id=step_num)
        context = {'ingredients': ingredients, 'recipe_pk': int(recipe_pk), 'step_num': int(step_num), 'stepRecipe':stepRecipe}
        return render(request, "base/ingredientlist.html", context)



class CreateIngredient(View):
    def get(self, request, recipe_pk, step_num):
        form = IngredientForm()
        context = {'form': form}
        return render(request, 'base/ingredient_form.html', context)

    def post(self, request, recipe_pk, step_num):
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            data['stepRecipe'] = StepRecipe.objects.get(id=step_num, recipe=recipe_pk)
            obj = Ingredient.objects.create(**data)
            obj.save()
            return redirect(reverse('ingredient-list', kwargs={'recipe_pk': recipe_pk, 'step_num': step_num}))
        else:
            context = {'form': form}
            return render(request, 'base/ingredient_form.html', context)


class UpdateIngredient(FormView, View):
    template_name = 'base/ingredient_form.html'
    form_class = IngredientForm
    success_url = '/recipes/'

    def get(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = Ingredient.objects.get(id=ingredient_pk)
        form = IngredientForm(instance=ingredient)
        context = {'form': form}
        return render(request, 'base/ingredient_form.html', context)

    def post(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = Ingredient.objects.get(id=ingredient_pk)
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect(reverse('ingredient-list', kwargs={'recipe_pk': recipe_pk, 'step_num': step_num}))


class DeleteIngredient(View):
    def get(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
        context = {'ingredient': ingredient}
        return render(request, "base/delete_ingredient.html", context)

    def post(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
        ingredient.delete()
        return redirect(reverse('ingredient-list', kwargs={'recipe_pk': recipe_pk, 'step_num': step_num}))


class UpdateStep(View):
    def get(self, request, recipe_pk, step_pk):
        print(StepRecipe.objects.all())
        stepRecipe = get_object_or_404(StepRecipe, pk=step_pk)

        form = StepRecipeForm(instance=stepRecipe)
        context = {'form': form}
        return render(request, "base/step_form.html", context)

    def post(self, request, recipe_pk, step_pk):
        stepRecipe = get_object_or_404(StepRecipe, pk=step_pk)
        form = StepRecipeForm(request.POST, instance=stepRecipe)
        if form.is_valid():
            form.save()
            return redirect(reverse('step-list', kwargs={'recipe_pk': recipe_pk}))


class CreateStep(View):
    def get(self, request, recipe_pk):
        form = StepRecipeForm()
        context = {'form': form}
        return render(request, 'base/step_form.html', context)

    def post(self, request, recipe_pk):
        form = StepRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            obj = StepRecipe.objects.create(**data)
            obj.save()
            return redirect(reverse('recipe', kwargs={'recipe_pk': recipe_pk}))


class DeleteStep(View):

    def get(self, request, recipe_pk, step_pk):
        stepRecipe = get_object_or_404(StepRecipe, pk=step_pk)
        return render(request, 'base/delete_step.html', {'obj': stepRecipe})

    def post(self, request, recipe_pk, step_pk):
        stepRecipe = get_object_or_404(StepRecipe, pk=step_pk)
        stepRecipe.delete()
        return redirect(reverse('step-list', kwargs={'recipe_pk': recipe_pk}))
