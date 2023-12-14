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
     
    
    def create(self, request):
        deserialized = ProductSerializer(data = request.data)
        if deserialized.is_valid(raise_exception=True):
            deserialized.save()
            return Response(status=status.HTTP_200_OK)
        
    
    
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        category = Category.objects.all()
        serialized = CategorySerializer(category, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        try:
            products = Product.objects.filter(category=pk)
            # print(products.id)
            serialized =ProductSerializer(products, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        
    def create(self, request):
        deserialized = CategorySerializer(data = request.data)
        if deserialized.is_valid(raise_exception=True):
            deserialized.save()
            return Response(status=status.HTTP_200_OK)
    