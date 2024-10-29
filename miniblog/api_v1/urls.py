from rest_framework.routers import DefaultRouter, path # Ofrece todas las rutas disponibles (GET, PUT, DELETE, RETRIEVE, POST) a un view set que nosotros indiquemos.

from api_v1.views.products_api import ProductViewSet

from api_v1.views.products_api import ProductViewSet #, ProductApiView, ProductListCreateGenericApiView

from api_v1.views.emails import send_test_email, email_products_sender

# Utilizado para el ModelViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, 'products')

urlpatterns = [
    # path('products_apiview', ProductApiView.as_view(), name='products_apiview'),
    # path('product_apiview/<int:pk>', ProductApiView.as_view(), name='product_apiview_detail'),
    # path('product_generic_apiview/<int:pk>', ProductListCreateGenericApiView.as_view(), 
    # name='product_apiview_detail'),
    path('send_email', send_test_email, name='send_email'),
    path('email_product_sender/', email_products_sender, name='email_sender')

]

# Para el uso de ApiViews
urlpatterns += router.urls