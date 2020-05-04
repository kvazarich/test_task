from django.db import models
from model_utils import Choices

from test_task.signals import human_created, human_deleted


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        human_created.send(sender=self.__class__, pk=self.pk)

    def delete(self, *args, **kwargs):
        pk = self.pk
        super().save(*args, **kwargs)
        human_deleted.send(sender=self.__class__, pk=pk)
