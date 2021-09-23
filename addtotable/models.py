from django.db import models


class Person(models.Model):
    Cislo = models.IntegerField(blank=False)
    Film = models.TextField(max_length=255)
    Actor = models.TextField(max_length=255)
    Country = models.TextField(max_length=255)
    Rez = models.TextField(max_length=255)


