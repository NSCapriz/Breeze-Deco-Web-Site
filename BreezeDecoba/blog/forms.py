from django import forms

# Fomularios Blog
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
    consult = forms.CharField(label="Su consulta", widget=forms.Textarea)

class BusquedaProductForm(forms.Form):
    name_product = forms.CharField(label="Búsqueda rápida")


