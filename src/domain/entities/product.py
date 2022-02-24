from typing import Optional

from src.domain.value_objects.price import Price
from src.domain.value_objects.product_type import ProductType


class Product:
    price: Price
    type: ProductType

    def __init__(self, price: Optional[Price] = None, type: Optional[ProductType] = None):
        self.price = price or Price()
        self.type = type or ProductType.ACAI
