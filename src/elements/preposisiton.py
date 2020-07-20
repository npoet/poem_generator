"""Preposition element class"""

from .rule import Rule


class Preposition(Rule):
    def __init__(self, name: str):
        super().__init__(name)
