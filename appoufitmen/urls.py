from django.urls import path
from appoufitmen import views
urlpatterns = [
    path('', views.inicio, name="inicio")
]
