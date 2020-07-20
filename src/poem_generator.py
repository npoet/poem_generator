"""Poem generator mainfile"""

import re
from elements import Rule


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
        # use iterator to add raw instructions to Rules
        for i in range(len(rules) - 1):
            # regex to find all text between rules
            raw_def = re.search(f'{rules[i].name}:(.*?){rules[i+1].name}:', raw_instructions).group(1)
            rules[i].raw_definition = raw_def

        for rule in rules:
            print(rule.name, rule.raw_definition)

    return


if __name__ == '__main__':
    main()
