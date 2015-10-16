from django.db import models


# Create your models here.

class Messaggio (models.Model):
    messaggio = models.CharField(max_length=100, unique=True)
    risposta = models.TextField(max_length=1000)
    audio = models.BooleanField(default=False)
    immagine = models.BooleanField(default=False)