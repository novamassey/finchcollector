# Generated by Django 4.0.1 on 2022-01-12 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 1, 4, 53, 231983)),
        ),
        migrations.AddField(
            model_name='feeding',
            name='food',
            field=models.CharField(choices=[('M', 'mealworms'), ('S', 'seeds'), ('V', 'fresh veggies'), ('E', 'eggfood')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Bird Breakfast'), ('L', 'Birdy Lunch'), ('S', 'Baby Bird Snack'), ('D', 'Big Bird Dinner')], default='B', max_length=1),
        ),
    ]