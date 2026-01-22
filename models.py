from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name


class Household(models.Model):
    name = models.CharField(max_length=100) 
    address = models.TextField()  
 
    def __str__(self):
        return self.name


class Resident(models.Model):
    name = models.CharField(max_length=100)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name


class ResidentIngredientPreference(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    preference_level = models.CharField(max_length=50)  
 
    def __str__(self):
        return f'{self.resident.name} prefers {self.ingredient.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    instructions = models.TextField()  
 
    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)


class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    date = models.DateField()

    def __str__(self):
        return self.name


class WeeklyMealView(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    meals = models.TextField()  

    def __str__(self):
        return f'Meals for {self.day_of_week} in {self.meal_plan.name}'
