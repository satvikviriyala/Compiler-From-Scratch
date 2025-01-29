# ast.py
class Program:
    def __init__(self, function):
        self.function = function

class Function:
    def __init__(self, name, body):
        self.name = name
        self.body = body

class Return:
    def __init__(self, expr):
        self.expr = expr

class Constant:
    def __init__(self, value):
        self.value = value

class BinaryOp:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right