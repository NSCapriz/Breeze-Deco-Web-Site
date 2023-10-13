from django.shortcuts import render

# Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

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
            return render(request,"blog/index.html", {"mensaje": "Usuario o contraseña no válidos, por favor vuelva a intentarlo"},)
    form = AuthenticationForm()

    return render(request, "login/login.html", {"form": form})