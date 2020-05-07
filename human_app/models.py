from django.db import models
from model_utils import Choices

from test_task.signals import human_post_save, human_pre_delete


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
        human_post_save.send(sender=self.__class__, pk=self.pk)

    def delete(self, *args, **kwargs):
        pk = self.pk
        human_pre_delete.send(sender=self.__class__, pk=pk)
        super().delete(*args, **kwargs)

    class Meta:
        db_table = 'Human'
        managed = False
