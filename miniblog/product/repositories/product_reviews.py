from django.contrib.auth.models import User
from django.shortcuts import (
    get_object_or_404

)

from product.models import ProductReview
from product.repositories.product import ProductRepository
from typing import List, Optional

class ProductReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def get_by_id(self, id: int) -> Optional[ProductReview]:
        try:
            productReview = ProductReview.objects.get(id = id)

        except:
            productReview = None
        
        return productReview
    
    def create(self, product_id: int, author: User, text: str, rating: int) -> ProductReview:
        product_repo = ProductRepository()
        product = product_repo.get_by_id(product_id)
        
        review = ProductReview.objects.create(
            product = product,
            author = author,
            text = text,
            rating = rating  

        )

        return review
    
    def update(self, review_id: int, author: User, text: str, rating: int) -> ProductReview:
        review = get_object_or_404(ProductReview, id = review_id)

        review.author = author
        review.text = text
        review.rating = rating
        
        review.save()

        return review
    
    def delete(self, review: ProductReview):
        return review.delete()

        