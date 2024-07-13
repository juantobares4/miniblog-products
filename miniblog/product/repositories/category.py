from product.models import Category
from typing import List

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def get_by_id(self, id:int): # Filtrar Categorías por ID.
        try:
            category = Category.objects.get(id = id)
        except:
            category = None

        return category
    
    def create(self, name:str):
        new_category = Category.objects.create(
            name = name

        ) 

        return new_category
    
    def delete(self, category:Category):
        return category.delete()
    
    def update(self, category:Category, new_name:str):
        category.name = new_name

        category.save()