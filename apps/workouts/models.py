from os import name

from django.db import models
from django.contrib.auth.models import User


class Workout_type(models.Model):

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

class Workout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.ForeignKey(Workout_type, on_delete=models.PROTECT)

    date = models.DateField('Data')
    distace_km = models.DecimalField('Distancia_km', max_digits=5, decimal_places=2)
    duration_sec = models.IntegerField()
    pace_sec_km = models.IntegerField()
    speed_kmh = models.DecimalField('Velocidade_kmh', max_digits=4, decimal_places=2)
    hr_avg = models.SmallIntegerField()
    hr_max = models.SmallIntegerField()
    cadence_spm = models.SmallIntegerField()
    elavation_m = models.SmallIntegerField()
    calories = models.SmallIntegerField()
    rpe = models.SmallIntegerField()
    notes = models.TextField('Observações', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Workout_splits(models.Model):

    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    split_number = models.SmallIntegerField()
    distace_km = models.DecimalField('Distancia_km', max_digits=5, decimal_places=2)
    pace_sec_km = models.IntegerField()
    pace_sec_km = models.IntegerField()
    elavation_m = models.SmallIntegerField()
