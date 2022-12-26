from django.shortcuts import render, redirect
from .models import Recipe, StepRecipe, Ingredient
from .forms import RecipeForm, StepRecipeForm, IngredientForm
from django.core.paginator import Paginator


def home(request):
    return render(request, 'base/home.html')


def recipes(request):
    allRecipes = Recipe.objects.all()
    context = {'allRecipes': allRecipes}
    return render(request, 'base/recipes.html', context)


def recipe(request, pk):
    selectedRecipe = Recipe.objects.get(id=pk)
    context = {'selectedRecipe': selectedRecipe}
    return render(request, 'base/recipe.html', context)


def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(form)
            nm = form.cleaned_data.get("name")
            cat = form.cleaned_data.get("category")
            dif = form.cleaned_data.get("difficulty")
            st = form.cleaned_data.get("steps")
            dur = form.cleaned_data.get("duration")
            img = form.cleaned_data.get("image")
            obj = Recipe.objects.create(
                name=nm,
                category=cat,
                difficulty=dif,
                duration=dur,
                steps=st,
                image=img
            )
            print(obj)
            obj.save()
            return redirect('recipes')
        # else:
        #     form = {}
        #     return redirect('recipes')
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'base/delete.html', {'obj': recipe})


def listingStepRecipe(request, recipe_pk, step_pk):
    recipe = Recipe.objects.get(id=int(recipe_pk))
    stepsRecipe = recipe.steprecipe_set.all()
    paginator = Paginator(stepsRecipe, per_page=1)
    page_object = paginator.get_page(step_pk)
    context = {"page_obj": page_object, "recipe_id": recipe_pk}
    return render(request, "base/steplist.html", context)


def updateStep(request, recipe_pk, step_pk):
    recipe = Recipe.objects.get(id=int(recipe_pk))
    stepsRecipe = recipe.steprecipe_set.get(id=int(step_pk))
    form = StepRecipeForm(instance=stepsRecipe)
    if request.method == "POST":
        form = StepRecipeForm(request.POST, instance=stepsRecipe)
        if form.is_valid():
            form.save()
            url_current_step = f'http://127.0.0.1:8000/recipe/{int(recipe_pk)}/steplist/{step_pk}/'
            print(url_current_step)
            return redirect(url_current_step)
    context = {'form': form}
    return render(request, "base/step_form.html", context)


def createStepRecipe(request):
    # stepRecipe = StepRecipe.objects.get(id=pk)
    # form= StepRecipeForm(instance=stepRecipe)
    if request.method == 'POST':
        form = StepRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')
        else:
            form = StepRecipeForm()
            context = {'form': form}
            return render(request, 'base/stepRecipe_form.html', context)




# def stepsRecipe(request, recipe_pk):
#     # firstAppear = False
#     recipe = Recipe.objects.get(id=recipe_pk)
#     # stepsRecipe = recipe.steprecipe_set.all()
#     stepsRecipe = recipe.steprecipe_set.first()
#     next_page = stepsRecipe.id+1
#     print(stepsRecipe)
#     firstAppear = True
#     # stepRecipes = StepRecipe.object.all()
#     context = {'recipe': recipe, 'stepsRecipe': stepsRecipe, 'next_page': next_page}
#     return render(request, 'base/stepsRecipe.html', context)
#

# def eachStepRecipe(request, recipe_pk, step_pk):
#     recipe = Recipe.objects.get(id=recipe_pk)
#     # stepsRecipe = recipe.steprecipe_set.all()
#     eachStepRecipe = recipe.steprecipe_set.get(id=step_pk)
#     print(eachStepRecipe.id)
#     next_page = eachStepRecipe.id + 1
#     context = {'recipe': recipe, 'eachStepRecipe': eachStepRecipe, 'next_page':next_page}
#     return render(request, 'base/eachStepRecipe.html', context)

