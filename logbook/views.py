from django.shortcuts import render, HttpResponse
from models import Logbook as lob_db
from django.views import generic
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
        return HttpResponse(value)
    else:
        pass