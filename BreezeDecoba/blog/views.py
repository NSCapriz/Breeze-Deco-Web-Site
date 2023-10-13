from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Client, Product, Category, Contacto, Avatar
from blog.forms import ClientForm, ProductForm, CategoryForm, ContactoForm, BusquedaProductForm

# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from blog.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

#CBV
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def inicio(request):
    #avatares = Avatar.objects.filter(user=request.user.id)[0]
    return render(request, "blog/index.html")#,{"url": avatares}

def nosotros(request):
    if request.method == 'POST':

        categoryForm = CategoryForm(request.POST)
        print(categoryForm)

        if categoryForm.is_valid():
            information = categoryForm.cleaned_data
            product = Category(product=information['product'], category=information['category'], subcategory=information['subcategory'])
            product.save()
            return render(request, "blog/productos.html")
    else:
        categoryForm = CategoryForm()
    return render(request, "blog/nosotros.html", {"categoryForm": categoryForm})

def productos(request):
    if request.method == 'POST':

        productoForm = BusquedaProductForm(request.POST)
        print(productoForm)

        if productoForm.is_valid():
            information = productoForm.cleaned_data
            productos = Product.objects.filter(name_product__icontains=information["name_product"])
    
            return render(request, "blog/resultadobusqueda.html", {"productos": productos})
        else:
            return render(request, "blog/productos.html", {"mensaje": "Lo sentimos, no contamos con ese producto."})
    else:
        productoForm = BusquedaProductForm()
    return render(request, "blog/productos.html", {"productoForm": productoForm})

def contacto(request):
    if request.method == 'POST':

        contactForm = ContactoForm(request.POST)
        print(contactForm)

        if contactForm.is_valid():
            information = contactForm.cleaned_data
            client = Contacto(user_name=information['user_name'], email=information['email'], consult=information['consult'])
            client.save()
            return render(request, "blog/index.html")
    else:
        contactForm = ContactoForm()
    return render(request, "blog/contacto.html",{"contactForm": contactForm})

def newsletter(request): #función a utilizar
    if request.method == 'POST':

        myForm = ClientForm(request.POST)
        print(myForm)

        if myForm.is_valid():
            information = myForm.cleaned_data
            client = Client(name=information['name'], lastname=information['lastname'], email=information['email'], age=information['age'])
            client.save()
            return render(request, "blog/index.html")
    else:
        myForm = ClientForm()
    return render(request, "blog/register.html", {"myForm": myForm})

# Función Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request,"blog/index.html",{"mensaje": f"Has iniciado sesión. Bienvenido {usuario}!"},)
            else:
                return render(request,"blog/index.html",{"mensaje": "Error, datos incorrectos"},)
        else:
            return render(request,"blog/index.html", {"mensaje": "Usuario o contraseña incorrectos, por favor vuelva a intentarlo"},)
    form = AuthenticationForm()

    return render(request, "blog/login.html", {"form": form})

# Función Registro
def registro(request):
    if request.method == "POST":
        registerForm = UserRegisterForm(request.POST)

        if registerForm.is_valid():
            username = registerForm.cleaned_data["username"]
            registerForm.save()
            return render(request, "blog/index.html", {"mensaje": "Su usuario ha sido registrado correctamente, ahora puede iniciar sesión"})

    else:
        registerForm = UserRegisterForm()

    return render(request, "blog/register.html", {"registerForm": registerForm})

#CBV-Clientes
class ClientListView(ListView):
    model = Client
    template_name = "blog/ClientesList.html"

class ClientDetailsView(DetailView):
    model = Client
    template_name = "blog/ClientesDetails.html"

class ClientCreateView(CreateView):
    model = Client
    template_name = "blog/ClientesCreate.html"
    success_url = reverse_lazy("ClientList")
    fields = ["name", "lastname", "email", "age"]

class ClientUpdateView(UpdateView):
    model = Client
    template_name = "blog/ClientesUpdate.html"
    success_url = reverse_lazy("ClientList")
    fields = ["name", "lastname", "email", "age"]

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("ClientList")
    template_name = "blog/ClientesDelete.html"


#CBV-Productos
class ProductListView(ListView):
    model = Product
    template_name = "blog/ProductosList.html"

class ProductDetailsView(DetailView):
    model = Product
    template_name = "blog/ProductosDetails.html"

class ProductCreateView(CreateView):
    model = Product
    template_name = "blog/ProductosCreate.html"
    success_url = reverse_lazy("ProductList")
    fields = ["name_product", "description", "price"]

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "blog/ProductosEdit.html"
    success_url = reverse_lazy("ProductList")
    fields = ["name_product", "description", "price"]

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("ProductList")
    template_name = "blog/ProductosDelete.html"

#CBV-Categorias
class CategoryListView(ListView):
    model = Category
    template_name = "blog/CategoryList.html"

class CategoryDetailsView(DetailView):
    model = Category
    template_name = "blog/CategoryDetails.html"

class CategoryCreateView(CreateView):
    model = Category
    template_name = "blog/CategoryCreate.html"
    success_url = reverse_lazy("CategoryList")
    fields = ["category", "subcategory", "product"]

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "blog/CategoryEdit.html"
    success_url = reverse_lazy("CategoryList")
    fields = ["category", "subcategory", "product"]

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("CategoryList")
    template_name = "blog/CategoryDelete.html"

#CBV-Contacto
class ContactoListView(ListView):
    model = Contacto
    template_name = "blog/ContactoList.html"

class ContactoDetailsView(DetailView):
    model = Contacto
    template_name = "blog/ContactoDetails.html"

class ContactoCreateView(CreateView):
    model = Contacto
    template_name = "blog/ContactoCreate.html"
    success_url = reverse_lazy("ContactoList")
    fields = ["user_name", "email", "consult"]

class ContactoUpdateView(UpdateView):
    model = Contacto
    template_name = "blog/ContactoEdit.html"
    success_url = reverse_lazy("ContactoList")
    fields = ["user_name", "email", "consult"]

class ContactoDeleteView(DeleteView):
    model = Contacto
    success_url = reverse_lazy("ContactoList")
    template_name = "blog/ContactoDelete.html"
    
#Edición Perfil User

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            if informacion["password1"] != informacion["password2"]:
                datos={
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)
            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()
                
                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=informacion['imagen'])
                    avatar.save()
                else:
                    avatar.imagen= informacion["imagen"]
                    avatar.save()
                return render(request, "blog/index.html")
    else:
        datos={
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "blog/usersProfile.html", {"miFormulario": miFormulario, "usuario": usuario})


# Author
def author(request):
    return render(request, "blog/author_view.html")