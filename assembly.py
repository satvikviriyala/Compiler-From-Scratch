# assembly.py
class Program:
    def __init__(self, functions):
        self.functions = functions

class Function:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class Label:
    def __init__(self, name):
        self.name = name

class Instruction:
    def __init__(self, opcode, operands):
        self.opcode = opcode
        self.operands = operands

class Move:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

class Add:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

class Sub:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

class Imul:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

class Idiv:
    def __init__(self, divisor):
        self.divisor = divisor

class Cmp:
    def __init__(self, src1, src2):
        self.src1 = src1
        self.src2 = src2

class Jmp:
    def __init__(self, target):
        self.target = target
    
class JmpCC:
    def __init__(self, condition, target):
        self.condition = condition
        self.target = target

class SetCC:
    def __init__(self, condition, dst):
        self.condition = condition
        self.dst = dst

class Ret:
    pass

class Push:
    def __init__(self, operand):
        self.operand = operand
    
class Pop:
    def __init__(self, operand):
        self.operand = operand

class Call:
    def __init__(self, fun_name):
        self.fun_name = fun_name

class Immediate:
    def __init__(self, value):
        self.value = value

class Register:
    def __init__(self, name):
        self.name = name

class Pseudo:
    def __init__(self, name):
        self.name = name

class Memory:
    def __init__(self, base, offset):
        self.base = base
        self.offset = offset