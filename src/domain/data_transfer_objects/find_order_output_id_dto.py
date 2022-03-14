from dataclasses import dataclass


@dataclass(frozen=True)
class FindOrderOutputIDDTO:
    order: str
