from tokens import *
from raise_error import *

OPERATORS = ('+', '-', '*', '/')


class Token(object):
    def __init__(self, type_, value):
        self.type = type_
        self.value = value


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def ignore_spaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token(FLOAT_CONST, result)
        else:
            return Token(INTEGER_CONST, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.ignore_spaces()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char in OPERATORS:
                op = self.current_char
                self.advance()
                return Token(OPERATOR, op)

            if self.current_char == '(':
                self.advance()
                return Token(L_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(R_PAREN, ')')

            raise_error(self.__class__.__name__, INV_CHAR,
                        char_pos=self.pos, char=self.current_char)

        return Token(EOF, None)
