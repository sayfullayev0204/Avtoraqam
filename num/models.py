from django.db import models
from hitcount.models import HitCountMixin, HitCount
# Create your models here.
class Num(HitCountMixin, models.Model):
    Hududiy_raqam = models.IntegerField()
    Nomer = models.CharField(max_length=6)
    Boshlanish_sanasi = models.DateField()
    Boshlanish_narxi = models.IntegerField()
    Malumot =  models.TextField()
    
    def __str__(self):
        return self.Nomer

class register(models.Model):
    name = models.CharField(max_length=220)
    password = models.CharField(max_length=200)
