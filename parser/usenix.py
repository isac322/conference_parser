#!/usr/bin/env python3
# coding: UTF-8

import argparse
import json
from urllib import request

from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser(description='Parse given URL to paper list as json format')
    parser.add_argument('url', metavar='URL', type=str, help='URL of workshop program')
    parser.add_argument('-o', '--output_file', dest='target', type=str,
                        help='instead of stdin, save result as json format to this file')

    args = parser.parse_args()

    result = list()

    page = request.urlopen(args.url)
    parsed = BeautifulSoup(page, 'html.parser')

    for elem in parsed.find_all('article', attrs={'class': 'node-session'}):
        paper_group = elem.find('div', attrs={'class': 'field-name-field-session-papers'})

        if not paper_group:
            continue

        section_name = elem.find('h2').text
        papers = list()

        for paper in paper_group.find('div', attrs={'class': 'field-items'}):
            title = paper.find('h2').a.text

            descriptions = paper.find('div', attrs={'class': 'field-name-field-paper-description-long'})
            description = '\n'.join(d.text for d in descriptions.find_all('p'))

            papers.append(dict(title=title, description=description))

        result.append(dict(section_name=section_name, papers=papers))

    if args.target:
        with open(args.target, 'w') as fp:
            json.dump(result, fp, indent=True, ensure_ascii=False)
    else:
        print(json.dumps(result, indent=True, ensure_ascii=False))


if __name__ == '__main__':
    main()
