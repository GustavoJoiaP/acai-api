import unittest

from src.domain.data_transfer_objects.request_order_input_dto import RequestOrderInputDTO
from src.domain.data_transfer_objects.request_order_output_dto import RequestOrderOutputDTO
from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository
from src.domain.services.request_order_service import RequestOrderService
from src.domain.value_objects.garnish import Garnish
from src.domain.value_objects.order_id import OrderID
from src.domain.value_objects.product_type import ProductType
from src.domain.value_objects.size import Size


class DummyOrderRepository(OrderRepository):
    count: int = 0

    def save(self, order: Order):
        self.count = self.count + 1
        order = order
        return order

    def select_all(self) -> list[Order]:
        pass

    def find_by_id(self, id: OrderID) -> Order:
        pass


class TestRequestOrderService(unittest.TestCase):
    # If service save order
    def test_request_when_DTO_contain_valid_args_then_call_order_repository_save(self):
        dummy_order_repository = DummyOrderRepository()
        request_order_service = RequestOrderService(dummy_order_repository)
        request_order_input_dto = RequestOrderInputDTO(garnish=Garnish.BANANA.value,
                                                       size=Size.SMALL.value,
                                                       product_type=ProductType.ACAI.value)

        request_order_service.request(dto=request_order_input_dto)

        expected_save_value = 1
        self.assertEqual(1, expected_save_value)

    # Return dto with id that was created
    def test_request_when_DTO_contain_valid_args_then_return_order(self):
        dummy_order_repository = DummyOrderRepository()
        request_order_service = RequestOrderService(dummy_order_repository)
        request_order_input_dto = RequestOrderInputDTO(garnish=Garnish.BANANA.value,
                                                       size=Size.SMALL.value,
                                                       product_type=ProductType.ACAI.value)

        request_order_output_dto = request_order_service.request(dto=request_order_input_dto)

        expected_order_output_dto = RequestOrderOutputDTO(garnish=Garnish.BANANA.value,
                                                          size=Size.SMALL.value,
                                                          product_type=ProductType.ACAI.value)

        self.assertEqual(expected_order_output_dto, request_order_output_dto)


