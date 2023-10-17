import django.db
from rest_framework import serializers
from inventory.models import Product, Category, Description

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    class Meta:
        model = Product
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
