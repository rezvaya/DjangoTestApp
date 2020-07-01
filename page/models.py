from django.db import models
from django.conf import settings
from django.utils import timezone

class Row(models.Model):
    value = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    value_type = models.CharField(max_length=200)
   
    def __str__(self):
        return self.value_type
