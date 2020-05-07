from django.db import models
from django.dispatch import receiver
from model_utils import Choices

from test_task.signals import human_post_save, human_pre_delete


@receiver(human_post_save)
def save_match(sender, pk, **kwargs):
    human = Human.objects.get(pk=pk)
    match, _ = Match.objects.get_or_create(human=human)
    match.gender = human.gender
    match.age = human.age
    match.first_name = human.first_name
    match.second_name = human.second_name
    match.save()


@receiver(human_pre_delete)
def delete_match(sender, pk, **kwargs):
    try:
        human = Human.objects.get(pk=pk)
    except Human.DoesNotExist:
        return
    match = Match.objects.get(human=human)
    match.delete()


class ImageField(models.ImageField):
    def value_to_string(self, obj):
        return obj.fig.url


class Human(models.Model):
    GENDER = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    avatar = ImageField(upload_to='images')
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER)

    class Meta:
        db_table = 'Human'
        managed = False


class Match(models.Model):
    GENDER = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER)
    human = models.OneToOneField(Human, primary_key=True, on_delete=models.DO_NOTHING)
