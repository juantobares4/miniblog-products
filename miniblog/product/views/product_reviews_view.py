from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.forms import ProductReviewForm
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,

)

from django.utils.translation import (
    activate,
    get_language,
    gettext_lazy as _,
    deactivate

)

from django.utils.decorators import method_decorator
from django.views import View
from product.models import ProductReview 
from product.repositories.product import ProductRepository
from product.repositories.product_reviews import ProductReviewRepository
from users.models import Profile

@method_decorator(login_required(login_url='login'), name='dispatch') # Da error si quiero acceder al método sin logearme. Debo estar logeado para acceder a él.
class ProductReviewView(View):
    def get(self, request):

        if not request.user.is_anonymous:
            user_profile = Profile.objects.get(user = request.user)
            selected_lang = user_profile.language
        
            activate(selected_lang  ) # Activa el lenguaje inglés en este caso.

        repo = ProductReviewRepository()
        reviews = repo.get_all()

        if not request.user.is_staff:
            reviews = reviews.filter(author = request.user)

        return render(
            request,
            'product_reviews/list.html',
            dict(
                reviews = reviews

            )

        )

class ProductReviewCreateView(View):
    def get(self, request, *args, **kwargs):
        repo_products = ProductRepository()
        all_products = repo_products.get_all()
        form = ProductReviewForm()
        
        return render(
            request,
            'product_reviews/create.html',
            dict(
                products = all_products,
                form = form,
                author = request.user

            )

        )

    def post(self, request):
        repo = ProductReviewRepository()
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            product_id = form.cleaned_data['product'].id
            review = form.cleaned_data['text']
            rating = form.cleaned_data['rating']
            author = request.user # El request almacena varios datos, entre ellos, el usuario que realizó la petición.

            repo.create(
                product_id = product_id,
                author = author,
                text = review,
                rating = rating

            )

            return redirect('product_reviews')

class ProductReviewDetailView(View):
    def get(self, request, id):
        review = get_object_or_404(
            ProductReview,
            id = id            

        )

        return render(
            request,
            'product_reviews/detail.html',
            dict(
                review = review

            )

        )
    
class ProductReviewUpdateView(View):
    def get(self, request, id):
        review = get_object_or_404(
            ProductReview, 
            id = id
        ) # Busca un objeto a través de el id que le pasemos, si no lo encuentra, devuelve un 404.

        form = ProductReviewForm(instance = review) # Objeto que buscamos a través del ID.

        return render(
            request,
            'product_reviews/update.html',
            dict(
                form = form,
                author = request.user

            )

        )

    def post(self, request, id):
        review_repository = ProductReviewRepository()
        review = get_object_or_404(
            ProductReview, 
            id = id
        
        )

        form = ProductReviewForm(request.POST, instance = review)

        if form.is_valid():
            opinion = form.cleaned_data['text']
            rating = form.cleaned_data['rating']
            author = User.objects.get(username = request.user)
            
            review_repository.update(
                review_id = review.id,
                author = author,
                text = opinion,
                rating = rating,
                
            )

            return redirect('product_review_detail', review.id)

class ProductReviewDeleteView(View):
    def get(self, request, id):
        filter_review = get_object_or_404(ProductReview, id = id)

        return render(
            request,
            'product_reviews/list.html',
            dict(
                filter_review = filter_review

            )

        )

    def post(self, request, id):
        review_repository = ProductReviewRepository()
        filter_review = review_repository.get_by_id(id = id)

        review_repository.delete(review = filter_review)

        return redirect('product_reviews') 