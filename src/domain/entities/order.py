from datetime import datetime
from typing import Optional

from src.domain.entities.product import Product
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.order_id import OrderID
from src.domain.value_objects.product_type import ProductType
from src.domain.value_objects.size import Size


class Order:
    id: OrderID
    garnish: Garnish
    size: Size
    created_at: datetime
    product: Product

    def __init__(self, garnish: Garnish, size: Size, product: Product, created_at: Optional[datetime] = None,
                 id: Optional[OrderID] = None):
        self.id = id or OrderID()
        self.created_at = created_at or datetime.now()
        self.garnish = garnish
        self.size = size
        self.product = product
