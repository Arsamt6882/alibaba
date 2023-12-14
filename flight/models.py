from django.db import models

class Flight(models.Model):
    origin=models.ForeignKey(a)
    name=models.CharField(max_length=255)
    no=models.CharField(max_length=22)
    capasity=models.IntegerField()
    price=models.FloatField()

class Airport(models.Model):
    name=models.CharField(max_length=234)
    no=models.CharField(max_length=24)
    city=models.IntegerField()
    address=models.IntegerField()
    phonenumber=models.IntegerField()
    opentime=models.CharField (max_length=11)
    closetime=models.CharField(max_length=6)

class bus(models.Model):
    name=models.CharField(max_length=234)
    no=models.CharField(max_length=24)
    price=models.FloatField()
