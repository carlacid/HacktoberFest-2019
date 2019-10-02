from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Bikes(models.Model):
    bike_name = models.CharField('Bike name', max_length=120)
    bike_model = models.CharField('Bike model', max_length=120)
    bike_horsepower = models.IntegerField(validators=[MinValueValidator(75),
                                                      MaxValueValidator(1250)])
    bike_description = models.TextField(max_length=250, blank=True)
