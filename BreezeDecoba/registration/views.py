from django.shortcuts import render

# Login
from registration.forms import UserRegisterForm

# Create your views here.

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

    return render(request, "registration/register.html", {"registerForm": registerForm})