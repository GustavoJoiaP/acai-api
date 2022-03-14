import unittest

from uuid import uuid4

from src.domain.data_transfer_objects.request_order_input_dto import RequestOrderInputDTO
from src.domain.data_transfer_objects.request_order_output_dto import RequestOrderOutputDTO
from src.domain.entities.order import Order
from src.domain.factories.order_factory import OrderFactory
from src.domain.repositories.order_repository import OrderRepository
from src.domain.services.request_order_service import RequestOrderService
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.order_id import OrderId
from src.domain.value_objects.product_type import ProductType
from src.domain.value_objects.size import Size


class DummyOrderRepository(OrderRepository):
    count: int = 0

    def save(self, order: Order):
        self.count = self.count + 1

    def select_all(self) -> list[Order]:
        pass

    def find_by_id(self, id: OrderId) -> Order:
        pass


class DummyOrderFactory(OrderFactory):
    order_id: OrderId

    def __init__(self, order_id: OrderId):
        self.order_id = order_id

    def build_new_order(self, garnish: str, size: str, product_type: str) -> Order:
        order = super().build_new_order(garnish, size, product_type)
        # order_id = OrderId(6)
        order.id = self.order_id
        return order


class TestRequestOrderService(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy_order_repository = DummyOrderRepository()

    # If service save order
    def test_request_when_DTO_contain_valid_args_then_call_order_repository_save(self):
        # Arrange
        order_id_value = uuid4()
        order_id = OrderId(order_id_value)
        dummy_order_factory = DummyOrderFactory(order_id=order_id)
        request_order_service = RequestOrderService(self.dummy_order_repository, dummy_order_factory)
        request_order_input_dto = RequestOrderInputDTO(garnish=Garnish.BANANA.value,
                                                       size=Size.SMALL.value,
                                                       product_type=ProductType.ACAI.value)
        # Action
        request_order_service.request(dto=request_order_input_dto)

        # Assert
        expected_save_value = 1
        self.assertEqual(expected_save_value, self.dummy_order_repository.count)

    # Return dto with id that was created
    def test_request_when_DTO_contain_valid_args_then_return_order(self):
        # Arrange
        order_id_value = uuid4()
        order_id = OrderId(order_id_value)
        dummy_order_factory = DummyOrderFactory(order_id=order_id)
        request_order_service = RequestOrderService(self.dummy_order_repository, dummy_order_factory)
        request_order_input_dto = RequestOrderInputDTO(garnish=Garnish.BANANA.value,
                                                       size=Size.SMALL.value,
                                                       product_type=ProductType.ACAI.value)
        # Action
        request_order_output_dto = request_order_service.request(dto=request_order_input_dto)

        # Assert
        expected_order_output_dto = RequestOrderOutputDTO(order_id=str(order_id_value))
        self.assertEqual(expected_order_output_dto, request_order_output_dto)
