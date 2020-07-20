"""Noun element class"""

from .rule import Rule


class Noun(Rule):
    def __init__(self, name: str):
        super().__init__(name)
