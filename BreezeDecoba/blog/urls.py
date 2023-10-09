from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_request, name="login"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos"),
    path('contacto/', views.contacto, name="contacto"),
    path("logout",LogoutView.as_view(template_name="blog/logout.html"), name="Logout",),
]
