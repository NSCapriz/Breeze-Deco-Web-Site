from django import forms
from .models import Post

# Fomularios Blog
class ClientForm(forms.Form):
    name = forms.CharField(label="Nombre")
    lastname = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    age = forms.DateField(label="Cumpleaños-(aaaa-mm-dd)")

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
    consult = forms.CharField(label="Su consulta", widget=forms.Textarea)

class BusquedaProductForm(forms.Form):
    name_product = forms.CharField(label="Búsqueda rápida")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        labels = {
            'title': 'Título del Post',
            'content': 'Mensaje',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
        }