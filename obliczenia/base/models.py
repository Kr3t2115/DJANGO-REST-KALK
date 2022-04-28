from re import T
from django.db import models

# Create your models here.
class obliczenie(models.Model):
    id  = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    pierwsza_liczba = models.CharField(max_length=200, null=False, blank=False)
    operator = models.CharField(max_length=200, null=False, blank=False)
    druga_liczba = models.CharField(max_length=200, null=False, blank=False)
    wynik_dzialania = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.id