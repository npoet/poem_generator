"""Line element class"""

from .rule import Rule


class Line(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.content = []
        self.rule_lst = []
        self.rule = ''

    def populate_rule_lst(self, rules: str):
        assert len(self.rule_lst) == 0
        split_rules = rules.split("|")
        self.rule_lst = [rule for rule in split_rules]

    def pick_rule(self):
        assert self.rule_lst != []
        self.rule = self.select_rand(self.rule_lst)[1:-1].lower().capitalize()
