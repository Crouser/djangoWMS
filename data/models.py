from django.db import models
from django.utils import timezone

class Data(models.Model):
    temperature = models.DecimalField(decimal_places = 2,max_digits = 100)
    pressure = models.DecimalField(decimal_places = 2,max_digits = 100)
    dateTime = models.DateTimeField(default=timezone.now)

  