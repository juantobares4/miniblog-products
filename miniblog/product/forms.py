from django import forms

from product.models import (
    Product,
    Category,
    Supplier,
    ProductReview,
    PriceHistory,
    ProductImage

)

class ProductForm(forms.ModelForm):
    class Meta: # Clase Meta Data donde se le dice el modelo y los campos del formulario.
        model = Product
        
        fields = [
            'name', 
            'category', 
            'price', 
            'stock', 
            'description'
        ] # Campos del formulario.
        
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'description': forms.Textarea(attrs = {'class': 'form-control'}),
            'price': forms.NumberInput(attrs = {'class': 'form-control'}),
            'category': forms.Select(attrs = {'class': 'form-control'}),
            'stock': forms.NumberInput(attrs = {'class': 'form-control'})

        } # Le da estilos a los campos.
        
        # fields = '__all__' # No recomendable: si se quiere agregar un campo nuevo no se puede, ya que esto trae todos los campos.

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier

        fields = [
            'name',
            'phone',
            'address'

        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control'}),
            'address': forms.TextInput(attrs = {'class': 'form-control'})

        }

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        
        fields = [
            'product',
            #'author',
            'text',
            'rating'

        ]

        widgets = {
            'product': forms.Select(attrs = {'class': 'form-control'}),
            #'author': forms.Select(attrs = {'class': 'form-control'}),
            'text': forms.Textarea(attrs = {'class': 'form-control'}),
            'rating': forms.NumberInput(attrs = {'class': 'form-control'})

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            'name'

        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'})

        }

class ProductImageForm(forms.ModelForm):
    class Meta: 
        model = ProductImage
        fields = [
            'product',
            'image',
            'description',

        ]