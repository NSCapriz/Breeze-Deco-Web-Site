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
