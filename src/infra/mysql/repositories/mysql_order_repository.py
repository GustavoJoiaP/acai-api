from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository


class MysqlOrderRepository(OrderRepository):
    def save(self, order: Order):
        pass

