from django.db import models

# Create your models here.


class Insecticide(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Herbicide(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Fungicide(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Bio_Fertilizer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Seed_Treatment(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name
