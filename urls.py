from django.urls import path
from . import views

urlpatterns = [
    path('households/', views.HouseholdListView.as_view(), name='household_list'),
    path('households/<int:pk>/', views.HouseholdDetailView.as_view(), name='household_detail'),
    path('residents/', views.ResidentListView.as_view(), name='resident_list'),
    path('residents/<int:pk>/', views.ResidentDetailView.as_view(), name='resident_detail'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('meal-plans/', views.MealPlanListView.as_view(), name='mealplan_list'),
    path('meal-plans/<int:pk>/', views.MealPlanDetailView.as_view(), name='mealplan_detail'),
]