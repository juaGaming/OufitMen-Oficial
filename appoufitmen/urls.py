from django.urls import path
from appoufitmen import views
from . views import*
from .viewsLogin import*
from .import viewsLogin

urlpatterns = [
    
    #Vistas Administrador
    path('InventarioAdmin',views.InventarioAdmin,name="InventarioAdmin"),
    path('InsertarPrendas/',InsertarProducto.as_view(),name='InsertarPrendas'),
    path('listarPrendas',ListarPrendas.as_view(), name='listarPrendas'),
    path('ActualizarProducto/<int:pk>',ActualizarProducto.as_view(), name='ActualizarProducto'),
    path('BuscarProducto/<int:pk>/', views.BuscarProducto.as_view(), name='BuscarProducto'),
    path('EliminarPrendas/<int:pk>',EliminarPrendas.as_view(),name='eliminar'),
    
    #Vistas Libres
    path('', views.inicio, name="Page_Inicio"),
    path('Casual/',views.Casual, name="RegistroUsuario"),
    path('Formal/',views.Formal, name="RegistroUsuario"),
    
    #Autenticacion
    path('Iniciar_Sesion/',viewsLogin.Iniciar_Sesion, name="Iniciar_Sesion"),
    path('RegistroUsuario/',viewsLogin.RegistrarUsuarios, name="RegistroUsuario"),
    path('Cerrar_Sesion/',viewsLogin.Cerrar_Sesion, name="RegistroUsuario"),
]
