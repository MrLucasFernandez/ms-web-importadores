from django.urls import path
from . import views

urlpatterns = [
    #path('',views.inicio, name=''),
    path('',views.ListarImportadores, name='importadores'),
    path('detalle/<str:pk>',views.FiltrarImportador, name='detalle'),
    path('crear', views.CrearImportador, name="crear"),
    path('actualizar/<str:pk>/', views.ActualizarImportador, name="actualizar"),
    path('eliminar/<str:pk>/', views.EliminarImportador, name="eliminar"),
    ]