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
]
