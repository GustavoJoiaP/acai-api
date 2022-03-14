from uuid import UUID

from src.domain.data_transfer_objects.find_order_input_id_dto import FindOrderInputIDDTO
from src.domain.data_transfer_objects.find_order_output_id_dto import FindOrderOutputIDDTO
from src.domain.entities.order import Order
from src.domain.exceptions.order_not_found_exception import OrderNotFoundException
from src.domain.repositories.order_repository import OrderRepository
from src.domain.value_objects.order_id import OrderId


class FindOrderService:
    __order_repository: OrderRepository

    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository

    def find_order_by_id(self, dto: FindOrderInputIDDTO) -> FindOrderOutputIDDTO:
        order_id = OrderId(UUID(dto.orderID))
        order = self.__order_repository.find_by_id(order_id)
        if order:
            # especificar dados de saida dto
            return FindOrderOutputIDDTO(order=order)
        else:
            raise OrderNotFoundException()
