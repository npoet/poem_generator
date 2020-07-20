"""Poem element class"""

from .rule import Rule


class Poem(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.num_lines: int
