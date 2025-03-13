# parser.py
from ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def peek(self):
        if self.index + 1 < len(self.tokens):
            return self.tokens[self.index + 1]
        return None

    def expect(self, type):
        if self.current_token and self.current_token.type == type:
            token = self.current_token
            self.advance()
            return token
        else:
            raise ValueError(f"Expected {type} but found {self.current_token.type}")

    def parse(self):
        # Parse the program
        return self.program()

    def program(self):
        # Parse a program
        return Program(self.function_definition())

    def function_definition(self):
        # Parse a function definition
        self.expect("INT")
        name = self.expect("IDENTIFIER").value
        self.expect("LPAREN")
        self.expect("VOID")
        self.expect("RPAREN")
        self.expect("LBRACE")
        statement = self.statement()
        self.expect("RBRACE")
        return Function(name, statement)

    def statement(self):
        # Parse a statement
        if self.current_token.type == "RETURN":
            return self.return_statement()
        else:
            raise ValueError("Invalid statement")

    def return_statement(self):
        # Parse a return statement
        self.expect("RETURN")
        expr = self.exp()
        self.expect("SEMICOLON")
        return Return(expr)
   
    
    def factor(self):
        # Parse a factor
        if self.current_token.type == "INT_CONSTANT":
            value = self.current_token.value
            self.advance()
            return Constant(value)
        elif self.current_token.type == "LPAREN":
            self.advance()
            expr = self.exp()
            self.expect("RPAREN")
            return expr
        else:
            raise ValueError("Invalid factor")

    def term(self):
        # Parse a term
        left = self.factor()
        while self.current_token and (self.current_token.type == "STAR" or self.current_token.type == "SLASH"):
            operator = self.current_token.type
            self.advance()
            right = self.factor()
            left = BinaryOp(operator, left, right)
        return left
    
    def exp(self):
        # Parse an expression
        left = self.term()
        while self.current_token and (self.current_token.type == "PLUS" or self.current_token.type == "MINUS"):
            operator = self.current_token.type
            self.advance()
            right = self.term()
            left = BinaryOp(operator, left, right)
        return left