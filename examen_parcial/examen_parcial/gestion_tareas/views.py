from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# todas las funciones en django requieren el parametro request 

def index(request):
    return HttpResponse('Esta es mi primera vista')


# devolver un html 

def ingreso(request):
    return render(request,'gestion_tareas/ingreso.html')

