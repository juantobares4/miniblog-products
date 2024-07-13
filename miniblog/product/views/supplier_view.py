from django.shortcuts import (
    redirect, 
    render
    
)

from django.views import View
from product.forms import SupplierForm
from product.repositories.supplier import SupplierRepository

repo = SupplierRepository()

class SupplierList(View):
    def get(self, request):
        get_all = repo.get_all()

        return render(
            request, 
            'supplier/list.html',
            dict(
                suppliers = get_all

            )

        )

class SupplierCreate(View):
    def get(self, request):
        form = SupplierForm()

        return render(
            request,
            'supplier/create.html',
            dict(
                form = form

            )

        )
    
    def post(self, request):
        form = SupplierForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']

            new_supplier = repo.create(name, address, phone)

            return redirect('suppliers_list')
        
class SupplierUpdate(View):
    def get(self, request, id):
        get_supplier = repo.get_by_id(id = id)
        form = SupplierForm(instance = get_supplier)

        return render(
            request,
            'supplier/update.html',
            dict(
                form = form
            
            )

        )

    def post(self, request, id):
        supplier_filter = repo.get_by_id(id = id)
        form = SupplierForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']

            repo.update(
                supplier = supplier_filter, 
                name = name,
                address = address,
                phone = phone 

            )

        return redirect('supplier_detail', supplier_filter.id)

class SupplierDetail(View): 
    def get(self, request, id):
        filter_supplier = repo.get_by_id(id = id)

        return render(
            request,
            'supplier/detail.html',
            dict(
                supplier = filter_supplier

            )

        )
    
class SupplierDelete(View):
    def get(self, request, id):
        filter_supplier = repo.get_by_id(id = id)

        repo.delete(supplier = filter_supplier)

        return redirect('suppliers_list')