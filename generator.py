# generator.py
from tacky import Function, Return, Constant, BinaryOp
class TackyGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.temp_counter = 0

    def new_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp

    def generate(self):
        tacky_functions = []
        for function in self.ast.functions:
            tacky_functions.append(self.generate_function(function))
        return Program(tacky_functions)

    def generate_function(self, function):
        instructions = []
        for statement in function.body:
            instructions.extend(self.generate_statement(statement))
        return Function(function.name, instructions)

    def generate_statement(self, statement):
        if isinstance(statement, Return):
            return self.generate_return(statement)
        # Handle other statement types similarly

    def generate_return(self, return_statement):
        return_val = self.generate_expr(return_statement.expr)
        return [Return(return_val)]

    def generate_expr(self, expr):
        if isinstance(expr, Constant):
            return Constant(expr.value)
        elif isinstance(expr, BinaryOp):
            left = self.generate_expr(expr.left)
            right = self.generate_expr(expr.right)
            temp = self.new_temp()
            return BinaryOp(expr.operator, left, right, temp)
        # Handle other expression types similarly