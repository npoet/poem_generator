"""Verb element class"""

from .rule import Rule


class Verb(Rule):
    def __init__(self, name: str):
        super().__init__(name)

    wordlist = []

    def populate_wordlist(self, lst: [str]):
        assert len(self.wordlist) == 0
        split_words = lst.split("|")
        self.wordlist = [word for word in split_words]
