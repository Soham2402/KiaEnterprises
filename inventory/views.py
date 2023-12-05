from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, ProductsSerializer, CategorySerializer, CategoryProductSerializer
from inventory.models import Category, Image, Product

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serialized = ProductsSerializer(products, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request,pk):
        try:
            products = Product.objects.get(id=pk)
            serialized = ProductSerializer(products, many=False)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
     
    def destroy(self, request, pk):
        try:
            Product.objects.get(id = pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    # def update(self, request, pk):
    #     try:
    #         #This is working hard coded still need to figure out how to make this shit dynamic
    #         Product.objects.filter(id = pk).update(name = "Random Harkat")
    #         return Response(status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        deserialized = ProductSerializer(data = request.data)
        if deserialized.is_valid(raise_exception=True):
            deserialized.save()
            return Response(status=status.HTTP_200_OK)
        
    # def update(self, request, pk):
    #     try:
    #         product_instance = Product.objects.get(id=pk)
    #     except Product.DoesNotExist:
    #         return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        
    #     deserialized = ProductSerializer(product_instance, data=request.data, partial=True)

    #     if deserialized.is_valid(raise_exception=True):
    #         deserialized.save()
    #         return Response(status=status.HTTP_200_OK)

    # def create(self, request):
    #     product_data = request.data
    #     description_data = product_data.pop('description', {})  # Handle the description data
    #     image_data = product_data.pop('product_images', [])  # Handle the image data
    #     subproducts_data = product_data.pop('subproducts', [])  # Handle the subproduct data

    #     # Create the product
    #     product_serializer = ProductSerializer(data=product_data)
    #     if product_serializer.is_valid():
    #         product = product_serializer.save()
    #         # Create the related description
    #         Description.objects.create(product=product, **description_data)
    #         # Create the related images
    #         for image in image_data:
    #             Image.objects.create(product=product, **image)
    #         # Create the related subproducts
    #         for subproduct_data in subproducts_data:
    #             SubProduct.objects.create(product=product, **subproduct_data)
    #         return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
    #     return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        category = Category.objects.all()
        serialized = CategorySerializer(category, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        try:
            products = Product.objects.filter(category=pk)
            # print(products.id)
            serialized = CategoryProductSerializer(products, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        try:
            # Product.objects.filter(category=pk).delete()
            Category.objects.get(id=pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def create(self, request):
        deserialized = CategorySerializer(data = request.data)
        if deserialized.is_valid(raise_exception=True):
            deserialized.save()
            return Response(status=status.HTTP_200_OK)
        
    def update(self, request, pk):
        try:
            category_instance = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        deserialized = CategorySerializer(category_instance, data=request.data, partial=True)

        if deserialized.is_valid(raise_exception=True):
            deserialized.save()
            return Response(status=status.HTTP_200_OK)