"""Line element class"""

from .rule import Rule


class Line(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.rule_lst = []
        self.rule = ''

    def pick_rule(self):
        assert self.rule_lst != []
        self.rule = self.select_rand(self.rule_lst)[1:-1].lower().capitalize()
