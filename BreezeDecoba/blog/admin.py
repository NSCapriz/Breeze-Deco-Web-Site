from django.contrib import admin
from .models import Client, Product, Category, Contacto

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contacto)
