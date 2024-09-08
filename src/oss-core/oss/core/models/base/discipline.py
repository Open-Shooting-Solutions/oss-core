from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID, uuid4
from oss.core.message import BrokerConnection


@dataclass
class BaseDiscipline(ABC):
    # Each buzzer needs an uuid so we can keep track of the discipline in logging.
    # This is mostly for debugging.
    _identifier: UUID
