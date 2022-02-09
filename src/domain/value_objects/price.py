from dataclasses import dataclass, field
from decimal import Decimal

from src.domain.exceptions.price_below_zero_exception import PriceBelowZeroException


@dataclass(frozen=True)
class Price:
    value: Decimal = field(default_factory=Decimal)

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if self.value < 0:
            raise PriceBelowZeroException()
