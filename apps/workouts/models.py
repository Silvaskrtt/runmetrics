from os import name

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

class WorkoutType(models.Model):

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    color = models.CharField(max_length=7)

class Workout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT)

    date = models.DateField('Data')
    distance_km = models.DecimalField('Distancia_km', max_digits=5, decimal_places=2)
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

class WorkoutSplits(models.Model):

    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    split_number = models.SmallIntegerField()
    distance_km = models.DecimalField('Distancia_km', max_digits=5, decimal_places=2)
    pace_sec_km = models.IntegerField()
    pace_sec_km = models.IntegerField()
    elavation_m = models.SmallIntegerField()

class TrainingPlans(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_race = models.ForeignKey(
        'goals.Races',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='TrainingPlans',
    )

    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class PlanWorkouts(models.Model):

    training_plan = models.ForeignKey(TrainingPlans, on_delete=models.PROTECT)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.PROTECT)

    scheduled_date = models.DateTimeField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    pace_min_sec_km = models.IntegerField()
    pace_max_sec_km = models.IntegerField()
    duration_sec = models.IntegerField()
    notes = models.TextField('Observações', blank=True, null=True)

class Insights(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    type = models.CharField(max_length=20)
    message = models.TextField()
    value_change = models.DecimalField(max_digits=5, decimal_places=2)
    generated_at = models.DateTimeField(auto_now=True)
