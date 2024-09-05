import logging 
from django.shortcuts import (
    redirect,
    render,
    get_list_or_404,

)

from django.views import View
from product.forms import ProductImageForm
from product.models import ProductImage

loggers = logging.getLogger('custom')

class ProductImageView(View):
    def get(self, request):
        loggers.debug('Este es un mensaje de depuración.')
        
        form = ProductImageForm
        images = ProductImage.objects.all()

        return render(
            request,
            'product_images/list.html',
            dict(
                images = images

            )

        )