from django.db import models
from django.contrib.auth.models import User

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
    img_product = models.ImageField(upload_to='productos/', null=True, blank=True)
    
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
    date_consult = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_name} - {self.date_consult} - {self.consult}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    author_post = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ["-date_create"]
        
    def __str__(self):
        return f"{self.title}"
