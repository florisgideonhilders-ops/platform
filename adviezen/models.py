from django.conf import settings
from django.db import models


class Zaak(models.Model):
    octopus_zaaknummer = models.CharField(max_length=100, unique=True)
    onderwerp = models.CharField(max_length=200, blank=True)
    dictum = models.CharField(max_length=200, blank=True)
    advies_tekst = models.TextField()
    aangemaakt_op = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-aangemaakt_op']

    def __str__(self):
        return f"{self.octopus_zaaknummer} - {self.onderwerp or 'Onbekend onderwerp'}"


class SearchQuery(models.Model):
    gebruiker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    zoekterm = models.CharField(max_length=200)
    onderwerp_filter = models.CharField(max_length=200, blank=True)
    dictum_filter = models.CharField(max_length=200, blank=True)
    resultaten_telling = models.PositiveIntegerField(default=0)
    aangemaakt_op = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-aangemaakt_op']

    def __str__(self):
        return f"{self.gebruiker} zocht op '{self.zoekterm}'"
