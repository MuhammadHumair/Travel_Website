from django.db import models

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='static/images/', height_field=None, width_field=None, max_length=None)
    active = models.BooleanField()

    def __str__(self):
        return self.name
    