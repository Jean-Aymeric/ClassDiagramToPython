from abc import ABC, abstractmethod

from ebaz import EBaz
from icorge import ICorge


class IFoo(ABC):
    @abstractmethod
    def Corge(self) -> ICorge:
        pass

    @abstractmethod
    def Corge(self, corge: ICorge) -> None:
        pass

    @abstractmethod
    def addBaz(self, baz: EBaz) -> None:
        pass
