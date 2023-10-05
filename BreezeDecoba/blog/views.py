from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Client, Product, Category, Contacto
from blog.forms import ClientForm, ProductForm, CategoryForm, ContactoForm, BusquedaProductForm
# Create your views here.

def inicio(request):
    return render(request, "blog/index.html")

def login(request):
    return render(request, "blog/login.html")

def registro(request):
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



