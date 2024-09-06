from rest_framework.routers import DefaultRouter # Ofrece todas las rutas disponibles (GET, PUT, DELETE, RETRIEVE, POST) a un view set que nosotros indiquemos.

from api_v1.views.products_api import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, 'products')

urlpatterns = router.urls
