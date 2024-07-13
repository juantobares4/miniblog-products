from django.urls import path

from product.views.product_view import (
    ProductList,
    ProductDetail,
    ProductUpdate,
    ProductDelete,
    ProductCreate,

)

from product.views.supplier_view import (
    SupplierList,
    SupplierCreate,
    SupplierUpdate,
    SupplierDetail,
    SupplierDelete

)

from product.views.category_view import (
    CategoryList,
    CategoryCreate,
    CategoryDetail,
    CategoryDelete,
    CategoryUpdate

)

from product.views.product_reviews_view import (
    ProductReviewCreateView,
    ProductReviewView,
    ProductReviewDetailView,
    ProductReviewUpdateView,
    ProductReviewDeleteView

)

from product.views.product_image_view import ProductImageView

urlpatterns = [
    # --- Rutas para Productos --- #
    path(route = '', view = ProductList.as_view(), name = 'product_list'),
    path(route = 'create/', view = ProductCreate.as_view(), name = 'product_create'), 
    path(route = '<int:id>/', view = ProductDetail.as_view(), name = "product_detail"),
    path(route = '<int:id>/update/', view = ProductUpdate.as_view(), name = "product_update"),
    path(route = '<int:id>/delete/',view = ProductDelete.as_view(), name = "product_delete"),
    
    # --- Rutas para Proveedores --- #
    path(route = 'suppliersList/', view = SupplierList.as_view(), name = 'suppliers_list'),
    path(route = 'supplier/supplierCreate/', view = SupplierCreate.as_view(), name = "supplier_create"),
    path(route = '<int:id>/supplierUpdate/', view = SupplierUpdate.as_view(), name = "supplier_update"),
    path(route = '<int:id>/supplierDetail/', view = SupplierDetail.as_view(), name = "supplier_detail"),
    path(route = '<int:id>/supplierDelete/', view = SupplierDelete.as_view(), name = "supplier_delete"),

    # --- Rutas para Categorías --- #
    path(route = 'categoryList/', view = CategoryList.as_view(), name = "category_list"),
    path(route = 'category/categoryCreate/', view = CategoryCreate.as_view(), name = "category_create"),
    path(route = '<int:id>/categoryDelete/', view = CategoryDelete.as_view(), name = "category_delete"),
    path(route = '<int:id>/categoryDetail/', view = CategoryDetail.as_view(), name = "category_detail"),
    path(route = '<int:id>/categoryUpdate/', view = CategoryUpdate.as_view(), name = "category_update"),

    # --- Rutas para Reviews --- #
    path(route = 'product_reviews/', view = ProductReviewView.as_view(), name = 'product_reviews'),
    path(route = 'product_reviews/create', view = ProductReviewCreateView.as_view(), name = 'product_review_create'),
    path(route = 'product_reviews/<int:id>', view = ProductReviewDetailView.as_view(), name = 'product_review_detail'),
    path(route = 'product_reviews/<int:id>/update', view = ProductReviewUpdateView.as_view(), name = 'product_review_update'),
    path(route = 'product_reviews/<int:id>/delete', view = ProductReviewDeleteView.as_view(), name = 'product_review_delete'),
    
    # --- Ruta para Imágenes --- #
    path(route = 'product_images/', view = ProductImageView.as_view(), name = 'product_images')

]
