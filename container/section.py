# coding: UTF-8
from typing import Iterable, Tuple

from container.paper import Paper


class Section:
    def __init__(self, section_name: str, papers: Iterable[Paper]):
        self._name = section_name
        self._papers = tuple(papers)

    @property
    def name(self) -> str:
        return self._name

    @property
    def papers(self) -> Tuple[Paper, ...]:
        return self._papers
