from django.urls import path
from blog import views

# URLS views
urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos"),
    path('contacto/', views.contacto, name="contacto"),
    path('author', views.author, name="Author"),
    path('forum/', views.foro, name="foro"),
    path('pages/administracion', views.administracion, name="administracion"),
    path('pages/suscripciones', views.newsletter, name="suscripciones"),
    path('messages/', views.post_new, name='post_new'),
]


#URLS CBV-Clientes
urlpatterns += [
    path("pages/clientes/list/", views.ClientListView.as_view(), name="ClientList"),
    path("clientes/details/<int:pk>", views.ClientDetailsView.as_view(), name="ClientDetails"),
    path("clientes/new/", views.ClientCreateView.as_view(), name="ClienteNew"),
    path("clientes/delete/<int:pk>",views.ClientDeleteView.as_view(),name="ClientDelete",),
]

#URLS CBV-Productos
urlpatterns += [
    path("pages/productos/list/", views.ProductListView.as_view(), name="ProductList"),
    path("productos/details/<int:pk>", views.ProductDetailsView.as_view(), name="ProductDetails"),
    path("productos/new/", views.ProductCreateView.as_view(), name="ProductNew"),
    path("productos/edit/<int:pk>", views.ProductUpdateView.as_view(), name="ProductEdit"),
    path("productos/delete/<int:pk>",views.ProductDeleteView.as_view(),name="ProductDelete",),
]

#URLS CBV-Categorias
urlpatterns += [
    path("pages/categorias/list/", views.CategoryListView.as_view(), name="CategoryList"),
    path("categorias/details/<int:pk>", views.CategoryDetailsView.as_view(), name="CategoryDetails"),
    path("categorias/new/", views.CategoryCreateView.as_view(), name="CategoryNew"),
    path("categorias/edit/<int:pk>", views.CategoryUpdateView.as_view(), name="CategoryEdit"),
    path("categorias/delete/<int:pk>",views.CategoryDeleteView.as_view(),name="CategoryDelete",),
]

#URLS CBV-Contacto
urlpatterns += [
    path("pages/contacto/list/", views.ContactoListView.as_view(), name="ContactoList"),
    path("contacto/details/<int:pk>", views.ContactoDetailsView.as_view(), name="ContactoDetails"),
    path("contacto/delete/<int:pk>",views.ContactoDeleteView.as_view(),name="ContactoDelete",),
]


#URLS CBV-Foro
urlpatterns += [
    path("pages/forum/list/", views.ForumListView.as_view(), name="ForumList"),
    path("forum/details/<int:pk>", views.ForumDetailsView.as_view(), name="ForumDetails"),
    path("forum/new/", views.ForumCreateView.as_view(), name="ForumNew"),
    path("forum/edit/<int:pk>", views.ForumUpdateView.as_view(), name="ForumEdit"),
    path("forum/delete/<int:pk>",views.ForumDeleteView.as_view(),name="ForumDelete",),
]