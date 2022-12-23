from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def home(request):
    return render(request, 'base/home.html')


def recipes(request):
    allRecipes = Recipe.objects.all()
    context = {'allRecipes': allRecipes}
    print(context)
    return render(request, 'base/recipes.html', context)


def recipe(request, pk):
    selectedRecipe = Recipe.objects.get(id=pk)

    context = {'selectedRecipe': selectedRecipe}
    print(context)
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
    if request.method=="POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    context = {'form':form}
    return render(request, 'base/recipe_form.html', context)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    return render(request, 'base/delete.html', {'obj': recipe})

