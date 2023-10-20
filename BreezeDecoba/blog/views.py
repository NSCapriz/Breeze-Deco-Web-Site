from django.shortcuts import render, redirect
from blog.models import Client, Product, Category, Contacto, Post
from blog.forms import ClientForm, CategoryForm, ContactoForm, BusquedaProductForm, PostForm
from django.utils import timezone

# Autenticacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#CBV
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def inicio(request):   
    return render(request, "blog/index.html")

def nosotros(request):
    if request.method == 'POST':

        categoryForm = CategoryForm(request.POST)
        print(categoryForm)

        if categoryForm.is_valid():
            information = categoryForm.cleaned_data
            product = Category(product=information['product'], category=information['category'], subcategory=information['subcategory'])
            product.save()
            return redirect('productos')
    else:
        categoryForm = CategoryForm()
    return render(request, "blog/nosotros.html", {"categoryForm": categoryForm})

def productos(request):
    if request.method == 'POST':
        productoForm = BusquedaProductForm(request.POST)

        if productoForm.is_valid():
            information = productoForm.cleaned_data
            productos = Product.objects.filter(name_product__icontains=information["name_product"])
    
            if productos:
                return render(request, "blog/resultadobusqueda.html", {"productos": productos})
            else:
                context = "Lo sentimos, por el momento no contamos con ese producto."
                return render(request, "blog/no_resultados.html", {"context": context})
        else:
            # Manejar errores de formulario, si es necesario
            pass
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
            return redirect('contacto')
    else:
        contactForm = ContactoForm()
    return render(request, "blog/contacto.html",{"contactForm": contactForm})

def newsletter(request):
    if request.method == 'POST':

        newsletterForm = ClientForm(request.POST)
        print(newsletterForm)

        if newsletterForm.is_valid():
            information = newsletterForm.cleaned_data
            client = Client(name=information['name'], lastname=information['lastname'], email=information['email'], age=information['age'])
            client.save()
            return redirect('productos')
    else:
        newsletterForm = ClientForm()
    return render(request, "blog/suscripciones.html", {"newsletterForm": newsletterForm})

@login_required
def foro(request):
    posts = Post. objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/forum.html", context=context)

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_post = request.user
            post.date_create = timezone.now()
            post.save()
            return redirect('foro')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def author(request): # Author View
    return render(request, "blog/author_view.html")

@login_required
def administracion(request):
    return render(request, "blog/administración.html")

#CBV-Clientes
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "blog/ClientesList.html"

class ClientDetailsView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "blog/ClientesDetails.html"

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "blog/ClientesCreate.html"
    success_url = reverse_lazy("ClientList")
    fields = ["name", "lastname", "email", "age"]

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("ClientList")
    template_name = "blog/ClientesDelete.html"

#CBV-Productos
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "blog/ProductosList.html"

class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "blog/ProductosDetails.html"

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "blog/ProductosCreate.html"
    success_url = reverse_lazy("ProductList")
    fields = ["name_product", "description", "price", "img_product"]

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "blog/ProductosEdit.html"
    success_url = reverse_lazy("ProductList")
    fields = ["name_product", "description", "price", "img_product"]

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("ProductList")
    template_name = "blog/ProductosDelete.html"

#CBV-Categorias
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "blog/CategoryList.html"

class CategoryDetailsView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "blog/CategoryDetails.html"

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "blog/CategoryCreate.html"
    success_url = reverse_lazy("CategoryList")
    fields = ["category", "subcategory", "product"]

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "blog/CategoryEdit.html"
    success_url = reverse_lazy("CategoryList")
    fields = ["category", "subcategory", "product"]

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("CategoryList")
    template_name = "blog/CategoryDelete.html"

#CBV-Contacto
class ContactoListView(LoginRequiredMixin, ListView):
    model = Contacto
    template_name = "blog/ContactoList.html"

class ContactoDetailsView(LoginRequiredMixin, DetailView):
    model = Contacto
    template_name = "blog/ContactoDetails.html"

class ContactoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contacto
    success_url = reverse_lazy("ContactoList")
    template_name = "blog/ContactoDelete.html"  

#CBV - Foro
class ForumListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/ForumList.html"

class ForumDetailsView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/ForumDetails.html"

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/ForumCreate.html"
    success_url = reverse_lazy("ForumList")
    fields = ["title", "content", "author_post"]
    labels = {
            'title': 'Título del Post',
            'content': 'Mensaje',
        }

class ForumUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/ForumEdit.html"
    success_url = reverse_lazy("ForumList")
    fields = ["title", "content"]

class ForumDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ForumList")
    template_name = "blog/ForumDelete.html" 

