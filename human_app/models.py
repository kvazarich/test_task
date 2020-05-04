from django.db import models
from model_utils import Choices


class Human(models.Model):
    GENDER = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    avatar = models.ImageField(upload_to='images')
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER)
