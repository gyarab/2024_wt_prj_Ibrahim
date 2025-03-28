from django.db import models

class Ball(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(null=True, blank=True)
    weight =  models.IntegerField(null=True, blank=True)
    diameter =  models.IntegerField(null=True, blank=True)
    purpose = models.CharField(max_length = 70)
    brand = models.CharField(max_length = 70)
    def __str__(self):
     return f"{self.name} "
# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=300)
    
        
    def __str__(self):
     return f"{self.znacka} "