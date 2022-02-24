from abc import ABC, abstractmethod

from src.domain.entities.order import Order
from src.domain.value_objects.order_id import OrderID


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        # Por enquanto nao estamos preocupado com atualizações
        pass

    @abstractmethod
    def select_all(self) -> list[Order]:
       # Retornar uma lista vazia caso nao tenha cadastro
        pass

    @abstractmethod
    def find_by_id(self, id: OrderID) -> Order:
        # Caso encotre uma order com id desejado, retornar instancia da order com so dados
        # Caso nao encontre order com o id desejado, lançar exception OrderNotFoundException
        pass
