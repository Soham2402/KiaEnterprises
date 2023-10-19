from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, ImageSerializer
from inventory.models import Category, Image, Product

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request,pk):
        try:
            products = Product.objects.get(id=pk)
            serialized = ProductSerializer(products, many=False)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request,pk):
        try:
            Product.objects.get(id = pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    # def update(self, request, pk):
    #     try:
    #         Product.objects.get(id = pk).update()
    #         return Response(status=status.HTTP_200_OK)
    #     except:
    #         return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(viewsets.ViewSet):
    pass
