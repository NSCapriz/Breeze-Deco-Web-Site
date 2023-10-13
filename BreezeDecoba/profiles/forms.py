from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario para perfil de usuario
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)
    last_name = forms.CharField(label="Nombre", required=False)
    first_name = forms.CharField(label="Apellido", required=False)
    imagen = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']