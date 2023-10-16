from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(null=False, max_length=256)
    price = models.PositiveIntegerField(null=False)
    hasSub = models.BooleanField(null=False)
    
    def __str__(self):
        return self.name
    
class Description(models.Model):
    about = models.TextField(null = False)
    dimension = models.CharField(max_length=256)
    weight = models.PositiveIntegerField()
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE, blank=True, null=True)
       
    def __str__(self):
        return self.about
    
    
class SubProduct(Product):
    sub_quality = models.CharField(max_length=256)
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE, related_name="subproducts")

    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    image = models.TextField(default="Test Image")
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE)
    
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=256)
    products = models.ForeignKey(to= Product, on_delete= models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    
    
    

    





    