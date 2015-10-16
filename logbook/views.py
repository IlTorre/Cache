from django.shortcuts import render, HttpResponseRedirect
from models import Logbook as lob_db
from django.views import generic
from django.core.urlresolvers import reverse
from forms import *
import datetime
from Cache import settings
# Create your views here.

class Logbook (generic.ListView):
    template_name = 'logbook/index.html'
    context_object_name = 'logbook'
    def get_queryset(self):

        return lob_db.objects.all().order_by('data')

def firma (request):
    if request.method=='GET':
        if request.COOKIES.has_key( 'accesso' ):
            value = request.COOKIES[ 'accesso' ]
            if value =='MARTIN PESCATORE':
                form=LogForm()
                return render(request,'logbook/firma.html',{'form':form})
        return render(request,'logbook/firma.html')
    else:
        form = LogForm(request.POST) #form bound to the POST data
        if form.is_valid(): # All validation rules pass
            log=form.save()
            return HttpResponseRedirect(reverse('logbook:logbook'))
        else:
            return render(request,'logbook/firma.html',{ 'form': form, 'messaggio':'Tutti i campi sono obbligatori' })