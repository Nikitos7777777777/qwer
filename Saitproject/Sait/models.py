from django.db import models

# Create your models here.
class car(models.Model):
    id = models.BigAutoField(primary_key=True)
    marka = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    def _str_(self):
        return f'{self.marka,self.cost}'

class Opisanie(models.Model):
    id = models.BigAutoField(primary_key=True)
    hourspower  = models.CharField(max_length=200)
    massa = models.CharField(max_length=200)
    spudi = models.CharField(max_length=200)

class Modelcar(models.Model):
    id = models.BigAutoField(primary_key=True)
    modele = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

class Complectacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    solon = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

class Enige(models.Model):
    id = models.BigAutoField(primary_key=True)
    volum = models.CharField(max_length=100)
    cylinders = models.CharField(max_length=100)
