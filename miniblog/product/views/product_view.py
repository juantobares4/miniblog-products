from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect, 
    render
    
)

from django.utils.decorators import method_decorator
from django.views import View
from product.forms import ProductForm
from product.models import Category
from product.repositories.product import ProductRepository

repo = ProductRepository()

class ProductList(View):
    def get(self, request):
        productos = repo.get_all()
        
        return render(
            request,
            'products/list.html',
            dict(
                products = productos
        
            )
    
        )

class ProductDetail(View):
    def get(self, request, id):
        producto = repo.get_by_id(id = id)
        
        return render(
            request,
            'products/detail.html',
            dict(
                product = producto
            
            )
        
        )

@method_decorator(login_required(login_url='login'), name='dispatch') # Tiene que ir method_decorator antes, ya que es un decorador para clases. En cambio, si solo ponemos login_required, este va para funciones por lo que nos dará error.
class ProductUpdate(View):
    def post(self, request, id):
        product = repo.get_by_id(id = id)
        form = ProductForm(request.POST, instance = product)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']
            id_category = form.cleaned_data['category'].id
            category = Category.objects.get(id = id_category)

            repo.update(
                producto = product,
                nombre = name,
                descripcion = description,
                precio = price,
                stock = stock,
                categoria = category

            )

            return redirect('product_detail', product.id)

    def get(self, request, id):
        product = repo.get_by_id(id = id)
        categorias = Category.objects.all()
        form = ProductForm(instance = product)

        return render(request,          
            'products/update.html', 
            dict(
                product = product,
                categories = categorias,
                form = form

            )

        )

class ProductDelete(View):
    def get(self, request, id):
        producto = repo.get_by_id(id = id)
        repo.delete(producto = producto)

        return redirect('product_list') # Nos retorna al listado de productos después de eliminar (lleva ese nombre en el archivo urls.py).

class ProductCreate(View):
    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            new_product = repo.create( # Toma el valor de los campos del formulario y el repositorio se encarga de crearlo en la base de datos. ES LA FORMA ÓPTIMA.
                nombre = form.cleaned_data['name'],
                precio = form.cleaned_data['price'],
                descripcion = form.cleaned_data['description'],
                cantidades = form.cleaned_data['stock'],
                categoria = form.cleaned_data['category'],

            )

            return redirect('product_list')

    def get(self, request):
        form = ProductForm()
        
        return render(request, 
            'products/create.html',
            dict(
                form = form
                
                )
            
            )
