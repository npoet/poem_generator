"""Verb element class"""

from .rule import Rule


class Verb(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.wordlist = []
        self.end_list = []

    def populate_wordlist(self, words: str):
        assert len(self.wordlist) == 0
        split_words = words.split("|")
        self.wordlist = [word for word in split_words]
