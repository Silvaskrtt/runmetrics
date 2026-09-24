import decimal

from django.db import models
from django.contrib.auth.models import User
from workouts.models import WorkoutType

class Goals(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    goal_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT)
    target_value = models.DecimalField('Valor da Meta', max_digits=8, decimal_places=2)
    current_value = models.DecimalField('Valor atual', max_digits=8, decimal_places=2)
    deadline = models.DateField()
    progress_pct = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GoalsType(models.Model):

    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=20)

class RaceType(models.Model):

    name = models.CharField(max_length=50)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)

class Races(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race_type = models.ForeignKey(RaceType, on_delete=models.PROTECT)
    
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    goal_time_sec = models.IntegerField()
    goal_time_sec = models.IntegerField()
    place = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
