from abc import ABC, abstractmethod
from typing import Any


class ICorge(ABC):
    @abstractmethod
    def Foo(self) -> Any:
        pass

    @abstractmethod
    def Foo(self, foo: Any) -> None:
        pass
