"""Adjective element class"""

from .rule import Rule


class Adjective(Rule):
    def __init__(self, name: str):
        super().__init__(name)
