from django.urls import path
from appoufitmen import views
from .viewsLogin import*
from .import viewsLogin

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('Casual/',views.Casual, name="RegistroUsuario"),
    path('Formal/',views.Formal, name="RegistroUsuario"),
    
    #Autenticacion
    path('Iniciar_Sesion/',viewsLogin.Iniciar_Sesion, name="Iniciar_Sesion"),
    path('RegistroUsuario/',viewsLogin.RegistrarUsuarios, name="RegistroUsuario"),
    path('Cerrar_Sesion/',viewsLogin.Cerrar_Sesion, name="RegistroUsuario"),
]
