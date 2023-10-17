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

class CategoryViewSet(viewsets.ViewSet):
    pass