# coding: UTF-8
from json import JSONEncoder

from container.paper import Paper
from container.section import Section


class PaperEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Paper):
            return dict(title=o.title, abstraction=o.abstractions)

        elif isinstance(o, Section):
            return dict(section_name=o.name, papers=[self.default(p) for p in o.papers])

        else:
            return super().default(o)
