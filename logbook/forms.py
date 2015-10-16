from django import forms
from  models import Logbook

class LogForm(forms.ModelForm):
    """
    Classe che implementa il form per il log
    """
    class Meta:
        model = Logbook
        fields = ['utente','log']