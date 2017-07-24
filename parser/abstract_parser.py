#!/usr/bin/env python3
# coding: UTF-8

import abc
from typing import List
from urllib import request

from bs4 import BeautifulSoup

from container.section import Section


class BaseParser(metaclass=abc.ABCMeta):
    def __init__(self, url: str):
        self.url = url

        page = request.urlopen(self.url)
        self._parsed_page = BeautifulSoup(page, 'html.parser')
        self._title: str = None

    @abc.abstractmethod
    def parse(self) -> List[Section]:
        pass

    @property
    @abc.abstractmethod
    def title(self) -> str:
        pass
