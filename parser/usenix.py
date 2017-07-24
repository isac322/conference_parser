# coding: UTF-8

import re
from typing import List

from container.paper import Paper
from container.section import Section
from parser.abstract_parser import BaseParser


class UsenixParser(BaseParser):
    @property
    def title(self) -> str:
        if not self._title:
            page_title = self._parsed_page.find('h1', attrs={'id': 'page-title'}).text
            self._title = re.search(r"(.+'\d{2})", page_title).group(1)

        return self._title

    def parse(self) -> List[Section]:
        result = list()

        for elem in self._parsed_page.find_all('article', attrs={'class': 'node-session'}):
            paper_group = elem.find('div', attrs={'class': 'field-name-field-session-papers'})

            if not paper_group:
                continue

            section_name = elem.find('h2').text
            papers = list()

            for paper in paper_group.find('div', attrs={'class': 'field-items'}):
                title = paper.find('h2').a.text

                abs_list = paper.find('div', attrs={'class': 'field-name-field-paper-description-long'})
                p_list = abs_list.find_all('p')

                if not p_list:
                    abstractions = (abs_list.text,)
                else:
                    abstractions = tuple(d.text for d in abs_list.find_all('p'))

                papers.append(Paper(title, abstractions))

            result.append(Section(section_name, papers))

        return result
