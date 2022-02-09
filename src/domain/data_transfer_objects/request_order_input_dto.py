from dataclasses import dataclass


@dataclass(frozen=True)
class RequestOrderInputDTO:
    garnish: str
    size: str
    product_type: str
