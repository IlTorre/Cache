from django.shortcuts import render
from django.http import HttpResponse
from models import Messaggio
# Create your views here.
def chat (request):
    if request.method == 'POST':
        messaggio=request.POST['messaggio']
        messaggio=messaggio.upper()
        risposta=Messaggio.objects.filter(messaggio=messaggio).last()
        if risposta == None:
            ris = 'Testo non riconosciuto'
            audio=False
            immagine=False
        else:
            ris=risposta.risposta
            audio=risposta.audio
            immagine=risposta.immagine
        var={'messaggio':messaggio,'risposta':ris,'audio':audio,'immagine':immagine}
        ret= render(request,'chat/home.html',var)
        ret.set_cookie(key='accesso',value=var['messaggio'],expires=1200)
        return ret
    else:
        var={'messaggio':'Cosa devo fare?',
             'risposta':'Benvenuto alla riserva Fontanili di Corte Valle Re! Esegui la prima istruzione indicata nel listening e scrivimi la risposta!'}
	return render(request,'chat/home.html',var)