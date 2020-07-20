"""Poem generator mainfile"""

import re
from elements import *


def main():
    # encapsulate file open for closure on clean-up
    with open("data/input.txt", "r") as f:
        # read entire file into str, strip newlines
        file_raw = f.read()
        raw_instructions = file_raw.replace('\n', ' ')
        # use simple regex to get rules from raw by selecting words preceding colon chars
        rule_names = re.findall("(\w+) *:", raw_instructions)
        # list comp to generate rule objects from names
        rules = [Rule(name) for name in rule_names]
        # use iterator to add raw instructions to Rules (all but last rule)
        for i in range(len(rules) - 1):
            # regex to find all text between rules
            raw_def = re.search(f'{rules[i].name}:(.*?){rules[i+1].name}:', raw_instructions).group(1)
            rules[i].raw_definition = raw_def

        # above loops misses edge case where rule ends in EOF, so for the last rule:
        raw_def_last = re.search(f'{rules[-1].name}:(.*?)\Z', raw_instructions).group(1)
        rules[-1].raw_definition = raw_def_last

        elements = []
        for r in rules:
            # clean raw rule names to match classes
            rule_name = r.name.lower().capitalize()
            # raw rule to subclass
            cls = globals()[rule_name](rule_name)
            # update rule and append
            cls.raw_definition = r.raw_definition
            cls.raw_def_to_list()
            # populate wordlist where applicable
            if rule_name in SENTENCE_ELEMENTS:
                cls.populate_wordlist(cls.definition_lst[0])
            elements.append(cls)

        # create poem structure
        poem = elements[0]
        poem.num_lines = len(poem.definition_lst)

    return


if __name__ == '__main__':
    main()
