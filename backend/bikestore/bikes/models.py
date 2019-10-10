from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    """
    Base model with common fields
    """
    created_at = models.DateTimeField('created_at', auto_now_add=True, db_column='created_at')
    updated_at = models.DateTimeField('updated_at', auto_now=True, db_column='updated_at')

    class Meta:
        abstract = True


class BaseModel(AbstractBase):
    bike_name = models.CharField('Bike name', max_length=120)
    bike_model = models.CharField('Bike model', max_length=120)
    bike_horsepower = models.IntegerField(validators=[MinValueValidator(75),
                                                      MaxValueValidator(1250)])
    bike_description = models.TextField(max_length=250, blank=True)
    bike_color = models.CharField('Bike color', max_lenght=50)
