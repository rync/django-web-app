from django.contrib import admin
from .models import Ingredient, Household, Resident, ResidentIngredientPreference, Recipe, RecipeIngredient, MealPlan, WeeklyMealView

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Household)
admin.site.register(Resident)
admin.site.register(ResidentIngredientPreference)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(MealPlan)
admin.site.register(WeeklyMealView)