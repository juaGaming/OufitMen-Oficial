from django.urls import path
from appoufitmen import views
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('Casual/',views.Casual, name="RegistroUsuario"),
    path('Formal/',views.Formal, name="RegistroUsuario"),
]
