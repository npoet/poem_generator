"""Rule element class"""

import random


class Rule(object):
    raw_definition = ''
    definition_lst = []

    def __init__(self, name: str):
        self.name = name

    def raw_def_to_list(self):
        assert self.raw_definition is not None
        split_string = self.raw_definition.split(" ")
        # remove all empty strings from str split (leading and trailing spaces etc)
        lst = [x for x in split_string if x != '']
        self.definition_lst = lst

    @staticmethod
    def select_rand(lst: [str]):
        return random.choice(lst)
