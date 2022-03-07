from dataclasses import dataclass

from src.domain.entities.order import Order


@dataclass(frozen=True)
class FindOrderOutputIDDTO:
    order: Order
