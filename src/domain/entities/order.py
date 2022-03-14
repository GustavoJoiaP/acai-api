from datetime import datetime
from typing import Optional

from src.domain.entities.product import Product
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.size import Size


class Order:
    id: OrderId
    garnish: Garnish
    size: Size
    created_at: datetime
    product: Product

    def __init__(self, garnish: Garnish, size: Size, product: Product, created_at: Optional[datetime] = None,
                 id: Optional[OrderId] = None):
        self.id = id or OrderId()
        self.created_at = created_at or datetime.now()
        self.garnish = garnish
        self.size = size
        self.product = product
