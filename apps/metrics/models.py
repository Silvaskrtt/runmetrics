from django.contrib.auth.models import User
from django.db import models

class DailyMetrics(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateTimeField()
    sleep_quality = models.SmallIntegerField()
    energy = models.SmallIntegerField()
    legs_feeling = models.SmallIntegerField()
    breathing = models.SmallIntegerField()
    pain_level = models.SmallIntegerField()
    notes = models.TextField('Obersevações', blank=True, null=True)
