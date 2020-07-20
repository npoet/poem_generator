"""Poem generator mainfile"""

import re
from elements import *


def raw_to_name(word: str):
    if word in KEYWORDS:
        return word
    return word[1:-1].lower().capitalize()


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
                cls.populate_rule_lst(cls.definition_lst[1])
            elements.append(cls)

        # create poem structure, find poem in list by attr
        poem = next(elem for elem in elements if elem.name == 'Poem')
        line = next(elem for elem in elements if elem.name == 'Line')
        line.populate_rule_lst(line.definition_lst[0])
        poem.num_lines = len(poem.definition_lst)
        # create lines for poem
        for i in range(poem.num_lines):
            line_start_name = raw_to_name(line.select_rand(line.rule_lst))
            line_start_obj = next(elem for elem in elements if elem.name == line_start_name)
            line_start_word = line_start_obj.select_rand(line_start_obj.wordlist)
            line_start_rule = raw_to_name(line_start_obj.select_rand(line_start_obj.rule_lst))
            poem.lines.append({i: [line_start_word, line_start_rule]})

        # finish all lines
        for i in range(len(poem.lines)):
            while list(poem.lines[i].values())[0][-1] not in KEYWORDS:
                word = list(poem.lines[i].values())[0][-1]
                next_obj = next(elem for elem in elements if elem.name == word)
                next_word = next_obj.select_rand(next_obj.wordlist)
                next_rule = raw_to_name(next_obj.select_rand(next_obj.rule_lst))
                poem.lines[i][list(poem.lines[i].keys())[0]].pop(-1)
                poem.lines[i][list(poem.lines[i].keys())[0]].append(next_word)
                poem.lines[i][list(poem.lines[i].keys())[0]].append(next_rule)

        # write poem
        poem.write_poem_to_console()

    return


if __name__ == '__main__':
    main()
