from src.domain.repositories.order_repository import OrderRepository


class SelectAllOrdersService:
    __order_repository: OrderRepository

    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository

    def select_all_orders(self):
        self.__order_repository.select_all()
