import csv
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action # Los decoradores son métodos que adicionan funcionalidades a otros métodos.
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
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
    
    @action(detail=False, methods=['get'], url_path='download-products-csv')
    def download_csv(self, request):
        # Que va a retornar y como se va a llamar
        response = HttpResponse(content_type='text/csv') 
        response['Content-Disposition'] = 'attachment; filename = "products.csv"' # 
        
        file = csv.writer(response)

        for product in self.get_queryset():
            file.writerow(
                [
                    product.name, 
                    product.description, 
                    product.description, 
                    product.price, 
                    product.stock, 
                    product.category.name if product.category else 'No posee categoría'
                ]

            )

        return response
    
    @action(detail=False, methods=['get'], url_path='download-price-stock-csv')
    def download_price_stock(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = "total_price.csv"'

        file = csv.writer(response)

        for product in self.get_queryset():
            file.writerow(
            [
                product.name, product.price, product.stock, product.price * product.stock
            ]

        )

        return response
    
""" class ProductApiView(APIView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        product_id = self.kwargs['pk']

        if product_id:
            products = product.get(id = product_id)
            serializer = ProductSerializer(products)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ...

from rest_framework import generics
from rest_framework import mixins

class ProductListCreateGenericApiView(
    generics.GenericAPIView, 
    mixins.ListModelMixin, 
    mixins.CreateModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) """