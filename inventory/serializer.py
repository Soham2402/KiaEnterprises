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
        
    def create(self, validated_data):
        description_data = validated_data.pop('description')
        image_data = validated_data.pop('product_images')
        subproducts_data = validated_data.pop('subproducts')

        product = Product.objects.create(**validated_data)

        Description.objects.create(product=product, **description_data)
        for image in image_data:
            Image.objects.create(product=product, **image)
        for subproduct_data in subproducts_data:
            SubProduct.objects.create(product=product, **subproduct_data)
        return product
    
class ProductsSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    product_images = ImageSerializer(many = True)
    class Meta:
        model = Product
        fields = "__all__"
        
    def create(self, validated_data):
        description_data = validated_data.pop('description')
        image_data = validated_data.pop('product_images')

        product = Product.objects.create(**validated_data)

        Description.objects.create(product=product, **description_data)
        for image in image_data:
            Image.objects.create(product=product, **image)
        return product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryProductSerializer(serializers.ModelSerializer):
    about = serializers.CharField(source='description.about')
    product_image = ImageSerializer(many = True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'about']
        # fields = ['id', 'name', 'price', 'about', 'product_image']    
