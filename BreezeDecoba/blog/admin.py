from django.contrib import admin
from .models import Client, Product, Category, Contacto, Post

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contacto)
admin.site.register(Post)
