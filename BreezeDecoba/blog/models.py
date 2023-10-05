from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.DateField()
    
    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class Product(models.Model):
    name_product = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return f"{self.name_product} ${self.price}"
    
class Category(models.Model):
    category = models.CharField(max_length=20)
    subcategory = models.CharField(max_length=20)
    product = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category} - {self.subcategory} ---> {self.product}"
    
class Contacto(models.Model):
    user_name = models.CharField(max_length=40)
    email = models.EmailField()
    consult = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.user_name} - {self.consult}"