# coding: UTF-8
from typing import Tuple


class Paper:
    def __init__(self, title: str, abstractions: Tuple[str, ...]):
        self._title = title
        self._abstractions = abstractions

    @property
    def title(self) -> str:
        return self._title

    @property
    def abstractions(self) -> Tuple[str, ...]:
        return self._abstractions
