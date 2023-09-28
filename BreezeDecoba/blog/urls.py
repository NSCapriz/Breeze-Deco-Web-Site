from django.urls import path
from blog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login, name="login"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos"),
    path('contacto/', views.contacto, name="contacto"),
]
