from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientForm(forms.Form):
    name = forms.CharField(label="Nombre")
    lastname = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    age = forms.DateField(label="Edad-(aaaa-mm-dd)")
    
class ProductForm(forms.Form):
    name_product = forms.CharField(label="Nombre del producto")
    description = forms.CharField(label="Descripción")
    price = forms.IntegerField()
    
class CategoryForm(forms.Form):
    category = forms.CharField(label="Categoria")
    subcategory = forms.CharField(label="Sub-Categoria o Tipo de producto")
    product = forms.CharField(label="Producto")
    
class ContactoForm(forms.Form):
    user_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electrónico")
    consult = forms.CharField(label="Su consulta (Maximo 200 caracteres)")
    
class BusquedaProductForm(forms.Form):
    name_product = forms.CharField(label="Búsqueda rápida")

#Formulario de Registro
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
#Formulario para perfil de usuario
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
