from django.shortcuts import render
from .models import Recipe

total_recipes = [
    {'id': 1, 'name': 'Gemista', 'category': 'Ladera', 'difficulty': 'Medium', 'totalMinutes': 30, 'totalSteps': 2,
     'mainPhoto': 'photo-main', },
    {'id': 2, 'name': 'Traxanas', 'category': 'Ladera', 'difficulty': 'Medium', 'totalMinutes': 30, 'totalSteps': 2,
     'mainPhoto': 'photo-main', },
    {'id': 3, 'name': 'Pastitio', 'category': 'Ladera', 'difficulty': 'Medium', 'totalMinutes': 30, 'totalSteps': 2,
     'mainPhoto': 'photo-main', },
]
step_recipe = [
    {'id': 1, 'title': 'mageirema kima', 'Description': 'vazooume ligo nero sto ..', 'step-duration': 30,
     'Photo': 'photo1', 'Process-bar': 30},
    {'id': 2, 'title': 'mageirema kima', 'Description': 'vazooume ligo nero sto ..', 'step-duration': 30,
     'photo': 'photo1', 'process-bar': 30}
]

ingredients = [
    {'id': 1, 'ingredient': 'kima', 'Photo': 'photo1'},
    {'id': 2, 'ingredient': 'kima', 'Photo': 'photo1'},
    {'id': 3, 'ingredient': 'kima', 'Photo': 'photo1'},
]


def home(request):

    return render(request, 'base/home.html')


def recipes(request):
    allRecipes = Recipe.objects.all()
    context = {'allRecipes': allRecipes}
    print(context)
    return render(request, 'base/recipes.html', context)


def recipe(request, pk):
    selectedRecipe = None
    for i in total_recipes:
        if i['id'] == int(pk):
            selectedRecipe = i
    context = {'selectedRecipe': selectedRecipe}
    print(context)
    return render(request, 'base/recipe.html', context)
