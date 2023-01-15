from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, StepRecipe, Ingredient
from .forms import RecipeForm, StepRecipeForm, IngredientForm
from django.core.paginator import Paginator
from django.views import View
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.forms import modelformset_factory


# The first page of the app
class HomeView(View):
    def get(self, request):
        return render(request, 'base/home.html')


# View list of all recipes
class RecipeListView(View):
    def get(self, request):
        allRecipes = Recipe.objects.all()
        context = {'allRecipes': allRecipes}
        return render(request, 'base/recipes.html', context)


# Create a Recipe
class CreateRecipeView(View):
    def get(self, request):
        form = RecipeForm()
        context = {'form': form}
        return render(request, 'base/recipe_form.html', context)

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            data=form.cleaned_data
            obj = Recipe.objects.create(**data)
            print(obj)
            obj.save()
            return redirect('recipes')
        else:
            context = {'form': form}
            return render(request, 'base/recipe_form.html', context)

class RecipeView(View):
    def get(self, request, pk):
        selectedRecipe = Recipe.objects.get(id=pk)
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
        form = RecipeForm(request.POST, instance=recipe)
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

    def get(self, request, recipe_pk, step_pk):
        recipe = Recipe.objects.get(id=int(recipe_pk))
        stepsRecipe = recipe.steprecipe_set.order_by('step')
        paginator = Paginator(stepsRecipe, per_page=1)
        page_object = paginator.get_page(step_pk)

        context = {"page_obj": page_object, "recipe_id": recipe_pk, "step_pk": step_pk}
        return render(request, "base/steplist.html", context)


class IngredientListView(View):

    def get(self, request, recipe_pk, step_num):
        recipe = Recipe.objects.get(id=int(recipe_pk))
        stepRecipe = recipe.steprecipe_set.get(step=int(step_num))
        ingredients = stepRecipe.ingredient_set.filter(stepRecipe__step=stepRecipe.step).all()
        context = {'ingredients': ingredients, 'recipe_pk': int(recipe_pk), 'step_num': int(step_num)}
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
            data['stepRecipe'] = StepRecipe.objects.get(step=step_num,recipe=recipe_pk)
            obj = Ingredient.objects.create(**data)
            obj.save()
            return redirect(reverse('ingredient-list', kwargs={'recipe_pk':recipe_pk, 'step_num':step_num}))
        else:
            context = {'form': form}
            return render(request, 'base/ingredient_form.html', context)


class UpdateIngredient(FormView, View):
    template_name = 'base/ingredient_form.html'
    form_class = IngredientForm
    success_url = '/recipes/'

    def get(self, request, recipe_pk, step_num,ingredient_pk):
        ingredient = Ingredient.objects.get(id=ingredient_pk)
        form = IngredientForm(instance=ingredient)
        context = {'form': form}
        return render(request, 'base/ingredient_form.html', context)

    def post(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = Ingredient.objects.get(id=ingredient_pk)
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect(reverse('ingredient-list', kwargs={'recipe_pk':recipe_pk, 'step_num':step_num}))

class DeleteIngredient(View):
    def get(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
        context = {'ingredient': ingredient}
        return render(request, "base/delete_ingredient.html", context)
    def post(self, request, recipe_pk, step_num, ingredient_pk):
        ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
        ingredient.delete()
        return redirect(reverse('ingredient-list', kwargs={'recipe_pk':recipe_pk, 'step_num':step_num}))


def updateStep(request, recipe_pk, step_num):
    recipe = Recipe.objects.get(id=int(recipe_pk))
    stepsRecipe = recipe.steprecipe_set.get(step=int(step_num))
    print(type(stepsRecipe))
    # stepsRecipe = recipe.steprecipe_set.all()
    form = StepRecipeForm(instance=stepsRecipe)
    if request.method == "POST":
        form = StepRecipeForm(request.POST, instance=stepsRecipe)
        if form.is_valid():
            form.save()
            url_current_step = f'http://127.0.0.1:8000/recipe/{int(recipe_pk)}/steplist/{step_num}/'
            print(url_current_step)
            return redirect(url_current_step)
    context = {'form': form}
    return render(request, "base/step_form.html", context)


def createStep(request, recipe_pk, ):
    form = StepRecipeForm()
    if request.method == 'POST':
        form = StepRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            rc = form.cleaned_data.get("recipe")
            st = form.cleaned_data.get("step")
            tt = form.cleaned_data.get("title")
            ds = form.cleaned_data.get("description")
            dr = form.cleaned_data.get("duration")
            img = form.cleaned_data.get("image")
            obj = StepRecipe.objects.create(
                recipe=rc,
                step=st,
                title=tt,
                description=ds,
                duration=dr,
                image=img
            )
            print(obj)
            obj.save()
            return redirect('recipes')
    context = {'form': form}
    return render(request, 'base/step_form.html', context)


def deleteStep(request, recipe_pk, step_num):
    recipe = Recipe.objects.get(id=int(recipe_pk))
    stepsRecipe = recipe.steprecipe_set.get(step=int(step_num))
    if request.method == 'POST':
        stepsRecipe.delete()
        recipe = Recipe.objects.get(id=int(recipe_pk))
        stepsRecipe = recipe.steprecipe_set.all()
        paginator = Paginator(stepsRecipe, per_page=1)
        page_object = paginator.get_page(step_num)
        context = {"page_obj": page_object, "recipe_id": recipe_pk}
        return render(request, "base/steplist.html", context)
    return render(request, 'base/delete_step.html', {'obj': stepsRecipe})

