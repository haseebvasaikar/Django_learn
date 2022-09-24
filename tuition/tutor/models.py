from platform import release
from re import M
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    
class Musician(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    instrument=models.CharField(max_length=100)
    
class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
    
class sub_Person(Album):
    SHIRT_SIZES = (
        ('S','small'),
        ('M','medium'),
        ('L','large'),
    )
    name = Album.name
    shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)
    
    
class Runner(Album):
    MedalType = models.TextChoices('MedalType','GOLD SILVER BRONZE')
    name=Album.name
    medal=models.CharField(blank=True,choices=MedalType.choices,max_length=10)
    
    
    