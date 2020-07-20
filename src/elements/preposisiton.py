"""Preposition element class"""

from .rule import Rule


class Preposition(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.wordlist = []
        self.rule_lst = []

    def populate_wordlist(self, words: str):
        assert len(self.wordlist) == 0
        split_words = words.split("|")
        self.wordlist = [word for word in split_words]

    def populate_rule_lst(self, rules: str):
        split_rules = rules.split("|")
        self.rule_lst = [rule for rule in split_rules]
