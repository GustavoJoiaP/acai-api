from src.domain.entities.order import Order
from src.domain.entities.product import Product
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.product_type import ProductType
from src.domain.value_objects.size import Size


class OrderFactory:

    def build_new_order(self, garnish: str, size: str, product_type: str) -> Order:
        garnish = Garnish(garnish)
        size = Size(size)
        product_type = ProductType(product_type)
        product = Product(type=product_type)
        order = Order(garnish=garnish, size=size, product=product)
        return order
