from django.db import models

class Ball(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(null=True, blank=True)
    hmotnost =  models.IntegerField(null=True, blank=True)
    obvod =  models.IntegerField(null=True, blank=True)
    ucel = models.CharField(max_length = 70)
    znacka = models.ForeignKey('Znacka', on_delete=models.SET_NULL)
    def __str__(self):
     return f"{self.name} "
# Create your models here.

class Znacka(models.Model):
    znacka = models.CharField(max_length=300)
    
        
    def __str__(self):
     return f"{self.znacka} "