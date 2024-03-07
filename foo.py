from ebaz import EBaz
from ibar import IBar
from icorge import ICorge
from ifoo import IFoo
from iqux import IQux
from qux import Qux


class Foo(IFoo):
    __bar: IBar
    __bazs: [EBaz]
    __qux: IQux
    __corge: ICorge | None

    def __init__(self, bar: IBar):
        self.__bar = bar
        self.__qux = Qux()
        self.__bazs = []
        self.__corge = None

    @property
    def Corge(self) -> ICorge:
        return self.__corge

    @Corge.setter
    def Corge(self, corge: ICorge) -> None:
        self.__corge = corge
        if corge.Foo != self:
            corge.Foo = self

    @property
    def Qux(self) -> IQux:
        return self.__qux

    def addBaz(self, baz: EBaz) -> None:
        self.__bazs.append(baz)
