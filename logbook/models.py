# -*- coding: utf-8 -*
from django.db import models
from django.utils import timezone
# Create your models here.

class Logbook (models.Model):
    utente = models.CharField(max_length=50, unique=True)
    log = models.TextField(max_length=300)
    data = models.DateTimeField(default=timezone.now)
