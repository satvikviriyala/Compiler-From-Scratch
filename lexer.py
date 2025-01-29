# lexer.py
import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}: {self.value}"
        return f"{self.type}"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position] if self.source_code else None

    def advance(self):
        self.position += 1
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            if self.current_char is not None and (self.current_char == 'e' or self.current_char == 'E'):
                result += self.current_char
                self.advance()
                if self.current_char is not None and (self.current_char == '+' or self.current_char == '-'):
                    result += self.current_char
                    self.advance()
                while self.current_char is not None and self.current_char.isdigit():
                    result += self.current_char
                    self.advance()
                
                return Token("FLOAT_CONSTANT", float(result))
            
            return Token("FLOAT_CONSTANT", float(result))
        
        if self.current_char is not None and (self.current_char == 'l' or self.current_char == 'L'):
            result += self.current_char
            self.advance()
            return Token("LONG_CONSTANT", int(result))
        
        if self.current_char is not None and (self.current_char == 'u' or self.current_char == 'U'):
            result += self.current_char
            self.advance()
            return Token("UNSIGNED_CONSTANT", int(result))
        
        
        return Token("INT_CONSTANT", int(result))

    def identifier(self):
        result = ""
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return Token("IDENTIFIER", result)

    def lex(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                tokens.append(self.number())
            elif self.current_char.isalpha() or self.current_char == '_':
                token = self.identifier()
                if token.value == 'if':
                    tokens.append(Token("IF"))
                elif token.value == 'else':
                    tokens.append(Token("ELSE"))
                elif token.value == 'while':
                    tokens.append(Token("WHILE"))
                elif token.value == 'do':
                    tokens.append(Token("DO"))
                elif token.value == 'for':
                    tokens.append(Token("FOR"))
                elif token.value == 'return':
                    tokens.append(Token("RETURN"))
                elif token.value == 'int':
                    tokens.append(Token("INT"))
                elif token.value == 'long':
                    tokens.append(Token("LONG"))
                elif token.value == 'void':
                    tokens.append(Token("VOID"))
                elif token.value == 'char':
                    tokens.append(Token("CHAR"))
                elif token.value == 'float':
                    tokens.append(Token("FLOAT"))
                elif token.value == 'double':
                    tokens.append(Token("DOUBLE"))
                elif token.value == 'signed':
                    tokens.append(Token("SIGNED"))
                elif token.value == 'unsigned':
                    tokens.append(Token("UNSIGNED"))
                elif token.value == 'static':
                    tokens.append(Token("STATIC"))
                elif token.value == 'extern':
                    tokens.append(Token("EXTERN"))
                elif token.value == 'struct':
                    tokens.append(Token("STRUCT"))
                elif token.value == 'sizeof':
                    tokens.append(Token("SIZEOF"))
                
                
                
                else:
                    tokens.append(token)
            elif self.current_char == '+':
                tokens.append(Token("PLUS"))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token("MINUS"))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token("STAR"))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token("SLASH"))
                self.advance()
            elif self.current_char == '%':
                tokens.append(Token("PERCENT"))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token("EQ"))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token("SEMICOLON"))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token("LPAREN"))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token("RPAREN"))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token("LBRACE"))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token("RBRACE"))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token("COMMA"))
                self.advance()
            
            elif self.current_char == '!':
                tokens.append(Token("BANG"))
                self.advance()
            elif self.current_char == '&':
                tokens.append(Token("AMPERSAND"))
                self.advance()
            elif self.current_char == '|':
                tokens.append(Token("PIPE"))
                self.advance()
            elif self.current_char == '~':
                tokens.append(Token("TILDE"))
                self.advance()
            elif self.current_char == '<':
                tokens.append(Token("LT"))
                self.advance()
            elif self.current_char == '>':
                tokens.append(Token("GT"))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token("LBRACKET"))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token("RBRACKET"))
                self.advance()
            elif self.current_char == '.':
                tokens.append(Token("DOT"))
                self.advance()
            elif self.current_char == '?':
                tokens.append(Token("QUESTION"))
                self.advance()
            elif self.current_char == ':':
                tokens.append(Token("COLON"))
                self.advance()
            
            else:
                raise ValueError(f"Invalid character: {self.current_char}")
        return tokens