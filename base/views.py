from django.shortcuts import render

total_recipes = [
    {'id': 1, 'Name': 'Gemista', 'Category': 'Ladera', 'Difficulty': 'Medium', 'Total-minutes': 30, 'Total-steps': 2,
     'Main-photo': 'photo-main', },
    {'id': 2, 'Name': 'Traxanas', 'Category': 'Ladera', 'Difficulty': 'Medium', 'Total-minutes': 30, 'Total-steps': 2,
     'Main-photo': 'photo-main', },
    {'id': 3, 'Name': 'Pastitio', 'Category': 'Ladera', 'Difficulty': 'Medium', 'Total-minutes': 30, 'Total-steps': 2,
     'Main-photo': 'photo-main', },
]
step_recipe = [
    {'id': 1, 'title': 'Mageirema kima', 'Description': 'Vazooume ligo nero sto ..', 'Step-duration': 30,
     'Photo': 'photo1', 'Process-bar': 30},
    {'id': 2, 'title': 'Mageirema kima', 'Description': 'Vazooume ligo nero sto ..', 'Step-duration': 30,
     'Photo': 'photo1', 'Process-bar': 30}
]

ingredients = [
    {'id': 1, 'ingredient': 'kima', 'Photo': 'photo1'},
    {'id': 2, 'ingredient': 'kima', 'Photo': 'photo1'},
    {'id': 3, 'ingredient': 'kima', 'Photo': 'photo1'},
]


def home(request):
    context = {'stepRecipes': step_recipe}
    return render(request, 'base/home.html', context)


def recipes(request):
    context = {'trecipes': total_recipes}
    return render(request, 'base/recipes.html', context)


def recipe(request, pk):
    recipe = None
    for i in total_recipes:
        if i['id'] == int(pk):
            recipe = i
    context = {'trecipes': recipe}
    return render(request, 'base/recipe.html', context)
