from django.contrib import admin
from models import *

# Register your models here.
class Messaggi (admin.ModelAdmin):
    """
    Classe che definisce la visualizzazione delle aste nel lato amministrativo
    """
    fieldsets = [
        ('Messaggio:',{'fields':['messaggio']}),
        ('Risposta',{'fields':['risposta']}),
        ('Audio',{'fields':['audio']}),
        ('Immagine',{'fields':['immagine']}),
    ]
    list_display = ('messaggio','risposta','audio','immagine')

admin.site.register(Messaggio,Messaggi)