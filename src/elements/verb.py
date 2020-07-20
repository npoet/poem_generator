"""Verb element class"""

from .rule import Rule


class Verb(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.wordlist = []
        self.rule_lst = []
