from django.db import models

class Data(models.Model):
    temperature = models.IntegerField()
    pressure = models.IntegerField()
