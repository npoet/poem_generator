"""Poem element class"""

from .rule import Rule


class Poem(Rule):
    def __init__(self, name: str):
        super().__init__(name)
        self.num_lines: int
        self.lines = []

    def write_poem_to_console(self):
        for line in self.lines:
            for word in list(line.values())[0]:
                if word != '$END':
                    print(word, end=' ')
            print("")

    def write_poem_to_file(self, filename: str):
        with open(filename, "w") as f:
            for line in self.lines:
                for word in list(line.values())[0]:
                    if word != '$END':
                        f.write(word)
                f.write("")
