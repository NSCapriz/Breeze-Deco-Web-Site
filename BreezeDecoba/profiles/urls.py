from django.urls import path
from profiles import views

# URLS views
urlpatterns = [
    path('accounts/profile/', views.editarPerfil, name="EditarPerfil"),  
]