from django.contrib.auth.models import User
from django.db import models

from workouts.models import Workout

class RecordTypes(models.Model):

    name = models.CharField(max_length=50)
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)

class PersonalRecords(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_types = models.ForeignKey(RecordTypes, on_delete=models.PROTECT)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)

    value = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField()
