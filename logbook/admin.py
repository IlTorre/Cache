from django.contrib import admin
from models import *
# Register your models here.

class log (admin.ModelAdmin):
    """
    Classe che definisce la visualizzazione delle aste nel lato amministrativo
    """
    fieldsets = [
        ('Utente:',{'fields':['utente']}),
        ('Log',{'fields':['log']}),
        ('Data',{'fields':['data']}),
    ]
    list_display = ('utente','log','data')
    ordering = ['data']
admin.site.register(Logbook,log)