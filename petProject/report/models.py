from django.db import models

# Create your models here.

class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    pet_age = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

