from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=256, unique=True)
    # Makes admin panel look sexy   
    def __str__(self):
        return self.name

class Product(models.Model):
    #'id' acts as a tool to connect this model to other models
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(null=False, max_length=256)
    price = models.PositiveIntegerField(null=False)
    hasSub = models.BooleanField(null=False) 
    # Establishes models connection with category
    category = models.ForeignKey(to = Category, on_delete= models.DO_NOTHING, default=1)
     
    #Makes admin panel look sexy
    def __str__(self):
        return self.name
    
class Description(models.Model):
    about = models.TextField(null = False)
    dimension = models.CharField(max_length=256)
    weight = models.PositiveIntegerField()
    # Establishes models connection with Product
    # One to one connection as each product is expected to have unique description
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE, blank=True, null=True)
    # Makes admin panel look sexy   
    def __str__(self):
        return self.about
    
    
class SubProduct(models.Model):
    sub_quality = models.CharField(max_length=256)
    #Establishes models connection with Product
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE, related_name="subproducts", blank=True, null=True)
    image = models.TextField()
    # Makes admin panel look sexy   
    def __str__(self):
        return f"{self.sub_quality} {self.product.name}"
    
    
class Image(models.Model):
    image = models.ImageField(upload_to ='assets/products', blank=False, null=False)
    # Establishes models connection with Product and SubProduct
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE,related_name="product_images", blank=True, null=True)
    
    

    
    
    
    

    





    