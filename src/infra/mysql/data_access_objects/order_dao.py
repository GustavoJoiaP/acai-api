from __future__ import annotations
from dataclasses import dataclass

from src.domain.entities.order import Order


@dataclass(frozen=True)
class OrderDAO:
    id: str
    garnish: str

    @classmethod
    def from_entity(cls, entity: Order) -> OrderDAO:
        dao = OrderDAO(id=str(entity.id.value), garnish=entity.garnish.value)
        return dao

    def build_insert_query(self) -> str:
        return "INSERT INTO acai_api.order (id, garnish) values ('" + self.id + "', '" + self.garnish + "');"
