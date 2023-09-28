from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.DateField()
    image = models.ImageField()
    password = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.name} {self.lastname}"

class Login(Client, models.Model):
    email = models.EmailField
    password = models.CharField(max_length=10)
    
class Product(models.Model):
    name_product = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self) -> str:
        return f"{self.name_product} - $ {self.price}"
    
class Category(models.Model):
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.category}, {self.subcategory}, {self.product}"
    
class Contacto(models.Model):
    options = [
        [0, "Consulta"],
        [1, "Reclamo"],
        [2, "Sugerencia"],
    ]
    user_name = models.CharField(max_length=40)
    email = models.EmailField()
    consult = models.IntegerField(choices=options)
    message = models.TextField()
    notice = models.BooleanField()