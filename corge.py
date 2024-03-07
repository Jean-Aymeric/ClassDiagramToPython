from typing import Any

from icorge import ICorge


class Corge(ICorge):
    __foo: Any | None  # Use Any due to cyclic dependency

    def __init__(self):
        self.__foo = None

    @property
    def Foo(self) -> Any | None:
        return self.__foo

    @Foo.setter
    def Foo(self, foo: Any) -> None:
        self.__foo = foo
