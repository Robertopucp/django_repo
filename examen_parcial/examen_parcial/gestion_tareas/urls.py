# crear rutas del proyecto

from . import views 
from django.urls import path 

app_name = 'gestion_tareas'

# se define las rutas de la aplicación

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login',views.login, name = 'login')
]
