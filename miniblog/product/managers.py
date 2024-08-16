from django.db import models

class ProductQuerySet(models.QuerySet): # Debe retornar una queryset. La herencia debe ser "models.QuerySet"
    def active(self):
        return self.filter(active=True) # Retorna self, para que no se haga un import "circular"
    
    def inactive(self):
        return self.filter(active=False)
    
    def total_price(self): # NO RETORNA UNA QUERYSET, sino un número.
        total = 0

        for product in self:
            total += product.price

        return total


