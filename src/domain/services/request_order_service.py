from src.domain.data_transfer_objects.request_order_input_dto import RequestOrderInputDTO
from src.domain.data_transfer_objects.request_order_output_dto import RequestOrderOutputDTO
from src.domain.factories.order_factory import OrderFactory
from src.domain.repositories.order_repository import OrderRepository


class RequestOrderService:
    __order_repository: OrderRepository
    __order_factory: OrderFactory

    def __init__(self, order_repository: OrderRepository, order_factory: OrderFactory):
        self.__order_repository = order_repository
        self.__order_factory = order_factory

    def request(self, dto: RequestOrderInputDTO) -> RequestOrderOutputDTO:
        order = self.__order_factory.build_new_order(dto.garnish, dto.size, dto.product_type)
        self.__order_repository.save(order)

        return RequestOrderOutputDTO(order_id=str(order.id.value))
