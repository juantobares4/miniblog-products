from product.models import Supplier
from typing import List, Optional

class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def get_by_id(self, id: int) -> Optional[Supplier]:
        return Supplier.objects.filter(id = id).first()

    def filter_by_address(self, address: str) -> List[Supplier]:
        return Supplier.objects.filter(address = address)

    def create(self, name: str, address: str, phone: str):
        return Supplier.objects.create(
            name = name,
            address = address,
            phone = phone

        )
    
    def delete(self, supplier: Supplier):
        return supplier.delete()
    
    def update(self, supplier: Supplier, name: str, address: str, phone: str):
        supplier.name = name
        supplier.address = address
        supplier.phone = phone

        supplier.save()

