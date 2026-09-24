from django.db import models
from django.contrib.auth.models import User

class Tools(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool_type = models.CharField(max_length=30)
    input_data = models.JSONField()
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
