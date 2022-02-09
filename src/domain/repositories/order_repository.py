from abc import ABC, abstractmethod

from src.domain.entities.order import Order


class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass
