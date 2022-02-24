from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository
from src.domain.services.request_order_service import RequestOrderService


class InMemoryOrderRepository(OrderRepository):
    __orders: list[Order]

    def __init__(self):
        self.__orders = list()

    def save(self, order: Order):
        self.__orders.append(order)

    def list(self):
        return self.__orders
