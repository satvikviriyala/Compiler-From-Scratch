# symbol_table.py
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, entry):
        self.symbols[name] = entry

    def get(self, name):
        return self.symbols.get(name)

    def contains(self, name):
        return name in self.symbols