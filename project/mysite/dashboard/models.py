from django.db import models

# Create your models here.
class dashboard(models.Model):
    car_type=models.CharField(max_length=200)
    journey=models.CharField(max_length=250)
