from django.db import models

# Create your models here.

class Destination(models.Model):
    '''
    This model is used to make the table for destination show on index page.
    '''
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    is_offer = models.BooleanField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
    