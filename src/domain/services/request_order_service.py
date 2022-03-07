from src.domain.data_transfer_objects.request_order_input_dto import RequestOrderInputDTO
from src.domain.data_transfer_objects.request_order_output_dto import RequestOrderOutputDTO
from src.domain.entities.order import Order
from src.domain.entities.product import Product
from src.domain.repositories.order_repository import OrderRepository
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.product_type import ProductType
from src.domain.value_objects.size import Size


class RequestOrderService:
    __order_repository: OrderRepository

    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository

    def request(self, dto: RequestOrderInputDTO) -> RequestOrderOutputDTO:
        garnish = Garnish(dto.garnish)
        size = Size(dto.size)
        product_type = ProductType(dto.product_type)
        product = Product(type=product_type)
        order = Order(garnish=garnish, size=size, product=product)
        self.__order_repository.save(order)
        
        return RequestOrderOutputDTO(order_id=str(order.id.value))
