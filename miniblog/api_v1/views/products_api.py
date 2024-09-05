from rest_framework.viewsets import ModelViewSet
from product.models import Product
from api_v1.serializers.product_serializers import ProductSerializer

class ProductViewSet(ModelViewSet): # ModelViewSet viene con todos los métodos incorporados (CRUD), mixins 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


