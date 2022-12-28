from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.recipe, name='recipe'),
    path('create-recipe/', views.createRecipe, name='create-recipe'),
    path('update-recipe/<str:pk>', views.updateRecipe, name='update-recipe'),
    path('delete-recipe/<str:pk>', views.deleteRecipe, name='delete-recipe'),

    # path('recipe/<str:recipe_pk>/steps-recipe/', views.stepsRecipe, name='steps-recipe'),
    # path('recipe/<str:recipe_pk>/steps-recipe/<str:step_pk>/', views.eachStepRecipe, name='step-recipe'),
    # path('recipe/<str:recipe_pk>/steplist/', views.listingStepRecipe, name='steplist'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_pk>/', views.listingStepRecipe, name='step-list'),
    path('recipe/<str:recipe_pk>/update-step/<int:step_num>/', views.updateStep, name='update-step'),
    path('recipe/<str:recipe_pk>/create-step/', views.createStep, name='create-step'),
    path('recipe/<str:recipe_pk>/delete-step/<int:step_num>/', views.deleteStep, name='delete-step'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients', views.listingIngrdient, name='ingredient-list'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/update-iningredients/', views.updateIngredient,
         name='update-ingredient'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/delete-iningredients/', views.deleteIngredient,
         name='delete-ingredient'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/create-iningredients/', views.createIngredient,
         name='create-ingredient'),
]
