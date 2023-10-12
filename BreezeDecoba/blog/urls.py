from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

# URLS views
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos"),
    path('contacto/', views.contacto, name="contacto"),
]

#URLS Registro,Login, Logout
urlpatterns += [
    path('registro/', views.registro, name="registro"),
    path('login/', views.login_request, name="login"),
    path("logout",LogoutView.as_view(template_name="blog/logout.html"), name="Logout"),
]

#URLS CBV-Clientes
urlpatterns += [
    path("clientes/list/", views.ClientListView.as_view(), name="ClientList"),
    path("clientes/details/<int:pk>", views.ClientDetailsView.as_view(), name="ClientDetails"),
    path("clientes/new/", views.ClientCreateView.as_view(), name="ClienteNew"),
    path("clientes/edit/<int:pk>", views.ClientUpdateView.as_view(), name="ClienteEdit"),
    path("clientes/delete/<int:pk>",views.ClientDeleteView.as_view(),name="ClientDelete",),
]

#URLS CBV-Productos
urlpatterns += [
    path("productos/list/", views.ProductListView.as_view(), name="ProductList"),
    path("productos/details/<int:pk>", views.ProductDetailsView.as_view(), name="ProductDetails"),
    path("productos/new/", views.ProductCreateView.as_view(), name="ProductNew"),
    path("productos/edit/<int:pk>", views.ProductUpdateView.as_view(), name="ProductEdit"),
    path("productos/delete/<int:pk>",views.ProductDeleteView.as_view(),name="ProductDelete",),
]

#URLS CBV-Categorias
urlpatterns += [
    path("categorias/list/", views.CategoryListView.as_view(), name="CategoryList"),
    path("categorias/details/<int:pk>", views.CategoryDetailsView.as_view(), name="CategoryDetails"),
    path("categorias/new/", views.CategoryCreateView.as_view(), name="CategoryNew"),
    path("categorias/edit/<int:pk>", views.CategoryUpdateView.as_view(), name="CategoryEdit"),
    path("categorias/delete/<int:pk>",views.CategoryDeleteView.as_view(),name="CategoryDelete",),
]

#URLS CBV-Contacto
urlpatterns += [
    path("contacto/list/", views.ContactoListView.as_view(), name="ContactoList"),
    path("contacto/details/<int:pk>", views.ContactoDetailsView.as_view(), name="ContactoDetails"),
    path("contacto/new/", views.ContactoCreateView.as_view(), name="ContactoNew"),
    path("contacto/edit/<int:pk>", views.ContactoUpdateView.as_view(), name="ContactoEdit"),
    path("contacto/delete/<int:pk>",views.ContactoDeleteView.as_view(),name="ContactoDelete",),
]

#URL Perfiles de Usuario
urlpatterns += [
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),     
]

#URL Author
urlpatterns += [
    path('author', views.author, name="Author"),     
]
