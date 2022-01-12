from django.db import models
#import reverse to use in the get_absolute_url function
from django.urls import reverse
# from django.utils import datetime


MEALS = (
    ('B', 'Bird Breakfast'),
    ('L', 'Birdy Lunch'),
    ('S', 'Baby Bird Snack'),
    ('D', 'Big Bird Dinner')
)

FOODS = (
    ('M', 'mealworms'),
    ('S', 'seeds'),
    ('V', 'fresh veggies'),
    ('E', 'eggfood')
)

# Create your models here.

# class Finch():
#     def __init__(self, name, type, color, species='bird'):
#         self.name = name 
#         self.type = type
#         self.color = color
#         self.species = species

# finches = [
#    Finch('Tweety', 'Hawfinch', 'Crimson'),
#    Finch('Polly', 'Hooded siskin', 'Yellow', 'Part Dinosaur'),
#    Finch('Greta', 'Elegant euphonia', 'Blue & Orange', 'Part Chicken') 
# ]        

class Finch(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    color = models.CharField(max_length = 100)
    species = models.TextField(max_length = 300)
    
    def __str__(self):
        return f"({self.id} - {self.name}"

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id}) 

class Feeding(models.Model):
    date = models.DateField('Feed Date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default = MEALS[0][0]
        )
    food = models.CharField(
        max_length=1,
        choices = FOODS,
        default = FOODS[1][0]) 
    finch = models.ForeignKey(Finch, on_delete = models.CASCADE)    

    def __str__(self):
        return f"A {self.get_meal_display()} of {self.get_food_display()} on {self.date}"          

