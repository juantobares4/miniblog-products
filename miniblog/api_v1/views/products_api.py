from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from api_v1.serializers.product_serializers import ProductSerializer
from api_v1.paginations import Pagination

class ProductViewSet(ModelViewSet): # ModelViewSet viene con todos los métodos incorporados (CRUD), mixins 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter] # Podemos agregar filtros de búsqueda en la URL
    search_fields = ['name', 'category__name'] # Debemos poner un lookup de category, ya que este campo no forma parte de producto.
    # pagination_class = Pagination    

    def create(self, request, *args, **kwargs):
        data = request.data # Extraemos los datos de la petición
        
        # Extraemos o creamos la categoría
        category_data = data.get('category')
        category_name = category_data.get('name')
        category, created = Category.objects.get_or_create(
            name = category_name
        
        )

        product = Product.objects.create(
            name = data.get('name'),
            description = data.get('description', None),
            price = data.get('price'),
            stock = data.get('stock'),
            active = data.get('active', True),    
            category = category or None

        )

        serializer = self.serializer_class(product)

        return Response(serializer.data, status.HTTP_201_CREATED) # Si no le pasamos un status, por defecto retornará un 200.

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)