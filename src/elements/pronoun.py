"""Pronoun element class"""

from .rule import Rule


class Pronoun(Rule):
    def __init__(self, name: str):
        super().__init__(name)
