from django.shortcuts import render
from profiles.models import  Avatar

# Login
from profiles.forms import UserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

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

    return render(request, "profiles/usersProfile.html", {"miFormulario": miFormulario, "usuario": usuario})
