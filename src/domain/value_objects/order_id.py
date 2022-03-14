from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class OrderId:
    value: UUID = field(default_factory=uuid4)



