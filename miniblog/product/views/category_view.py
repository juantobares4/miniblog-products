from django.shortcuts import (
    get_object_or_404,
    render, 
    redirect
    
)

from django.views import View
from product.forms import CategoryForm
from product.models import Category, Product
from product.repositories.category import CategoryRepository

repo = CategoryRepository()

class CategoryList(View):
    def get(self, request):
        all_categories = repo.get_all()

        return render(
            request,
            'categories/category_list.html',
            dict(
                categories = all_categories # categories es la variable que vamos a utilizar en el HTML. 
            
            )

        )

class CategoryCreate(View):
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']

            new_category = repo.create(name)

            return redirect('category_list')

    def get(self, request):
        form = CategoryForm

        return render(request,
            'categories/category_create.html',
            dict(
                form = form

            )

        )

class CategoryDetail(View):
    def get(self, request, id):
        category = repo.get_by_id(id = id)

        return render(
            request,
            'categories/category_detail.html',
            dict(
                category = category

            )

        )
    
class CategoryDelete(View):
    def get(self, request, id):
        filter_category_to_delete = repo.get_by_id(id = id)

        repo.delete(category = filter_category_to_delete)

        return redirect('category_list')

class CategoryUpdate(View):
    def get(self, request, id):
        category = get_object_or_404(
            Category,
            id = id

        )

        products = Product.objects.all()

        form = CategoryForm(instance = category)

        return render(request, 
            'categories/category_update.html',
            dict(
                form = form,
                products = products
            
            )
        
        )
    
    def post(self, request, id):
        category_filter = repo.get_by_id(id = id)
        
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            category_name = form.cleaned_data['name']
        
            repo.update(
                category = category_filter,
                new_name = category_name # La variable tiene que ir con el mismo nombre que en el repositorio.
            
            )

        return redirect('category_detail', category_filter.id)
    