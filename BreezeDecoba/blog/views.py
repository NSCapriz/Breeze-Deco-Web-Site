from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "blog/index.html")

def login(request):
    return render(request, "blog/login.html")

def registro(request):
    return render(request, "blog/register.html")

def nosotros(request):
    return render(request, "blog/nosotros.html")

def productos(request):
    return render(request, "blog/productos.html")

def contacto(request):
    return render(request, "blog/contacto.html")