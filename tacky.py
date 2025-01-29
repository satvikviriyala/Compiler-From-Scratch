# tacky.py
class Program:
    def __init__(self, functions):
        self.functions = functions

class Function:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class Return:
    def __init__(self, val):
        self.val = val

class Constant:
    def __init__(self, value):
        self.value = value

class BinaryOp:
    def __init__(self, operator, src1, src2, dst):
        self.operator = operator
        self.src1 = src1
        self.src2 = src2
        self.dst = dst