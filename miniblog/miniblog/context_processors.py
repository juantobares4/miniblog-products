# Nos permite agregar información al contexto de la aplicación. Es decir, podemos utilizarla desde cualquier lado.

from django.core.cache import cache
from product.models import Product, Category
from users.models import Profile

def all_names_products(request, ):
    products = cache.get('products')
    
    if products is None: # Si los productos no están en el cache, los busca en la base de datos. Y ahí procede a guardarlos en el caché.
        products = Product.objects.all().values_list('name') # values.list nos trae únicamente el valor name de la query set.
        cache.set('products', products, 36000) # El 36000 es el tiempo que queremos almacenar los datos en el caché.
    
    return dict(
        names = products

    )

def all_names_categories(request, ):
    categories = Category.objects.all()
    names = [category.name for category in categories]

    return dict(
        names_categories = names

    )

def profile_language(request, ):
    return dict(
        profile = Profile.objects.get(user=request.user)

    )