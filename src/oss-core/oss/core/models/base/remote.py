from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from oss.core.message import BrokerConnection
from oss.core.models.base.timer import TimerControl


class BaseRemote(ABC):
    # Each remote needs an uuid so we can keep track of which remote triggered an action.
    # This is mostly for debugging.
    _identifier: UUID = uuid4()

    # Each remote needs an connection to the message broker to send commands
    _broker_connection: BrokerConnection

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def __del__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _handle_hook_event(self, action: TimerControl) -> None:
        raise NotImplementedError

    @abstractmethod
    def _register_hooks(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _remove_hooks(self) -> None:
        raise NotImplementedError
