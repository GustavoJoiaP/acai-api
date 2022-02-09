from dataclasses import dataclass


@dataclass(frozen=True)
class RequestOrderOutputDTO:
    order_id: str

