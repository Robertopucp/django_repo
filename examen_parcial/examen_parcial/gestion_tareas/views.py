from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# todas las funciones en django requieren el parametro request 

def index(request):
    return HttpResponse('Esta es mi primera vista')


# devolver un html 

def login(request):

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        print('El usuario es:', str(usuario))
    return render(request,'gestion_tareas/login.html', {
        'nombre':'Roberto',
        'apellido':'Mendoza',
        'edad':'25'
    })


