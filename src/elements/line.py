"""Line element class"""

from .rule import Rule


class Line(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.content: [str]
