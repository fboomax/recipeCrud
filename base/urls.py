from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipe/<str:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('create-recipe/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('update-recipe/<str:pk>', views.UpdateRecipeView.as_view(), name='update-recipe'),
    path('delete-recipe/<str:pk>', views.DeleteRecipeView.as_view(), name='delete-recipe'),

    # path('recipe/<str:recipe_pk>/steps-recipe/', views.stepsRecipe, name='steps-recipe'),
    # path('recipe/<str:recipe_pk>/steps-recipe/<str:step_pk>/', views.eachStepRecipe, name='step-recipe'),
    # path('recipe/<str:recipe_pk>/steplist/', views.listingStepRecipe, name='steplist'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_pk>/', views.StepRecipeListView.as_view(), name='step-list'),
    path('recipe/<str:recipe_pk>/update-step/<int:step_num>/', views.updateStep, name='update-step'),
    path('recipe/<str:recipe_pk>/create-step/', views.createStep, name='create-step'),
    path('recipe/<str:recipe_pk>/delete-step/<int:step_num>/', views.deleteStep, name='delete-step'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients', views.IngredientListView.as_view(), name='ingredient-list'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/<int:ingredient_pk>/update/', views.UpdateIngredient.as_view(),
         name='update-ingredient'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/<int:ingredient_pk>/delete/', views.DeleteIngredient.as_view(),
         name='delete-ingredient'),
    path('recipe/<str:recipe_pk>/steplist/<int:step_num>/ingredients/create-iningredients/', views.CreateIngredient.as_view(),
         name='create-ingredient'),
]
