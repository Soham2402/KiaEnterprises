import django.db
from rest_framework import serializers
from inventory.models import Product, Category, Description, SubProduct, Image


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProduct
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    product_images = ImageSerializer(many = True)
    subproducts = SubProductSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
