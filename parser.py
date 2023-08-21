from tokens import *
from raise_error import *


class AST(object):
    pass


class Program(AST):
    def __init__(self):
        self.nodes_list = []


class Num(AST):
    def __init__(self, token):
        self.value = int(token.value)


class BinOp(AST):
    def __init__(self, left, op_token, right):
        self.left_node = left
        self.right_node = right
        self.operator = op_token.value


class AssignOp(AST):
    def __init__(self, var, right):
        self.var_node = var
        self.right_node = right


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type != token_type:
            raise_error(self.__class__.__name__, INV_SYNTAX)
        self.current_token = self.lexer.get_next_token()

    def program(self):
        """program: assign_statement
           assign_statement = variable ASSIGN expr
           variable: ID"""
        program_node = Program()

        while self.current_token.type != EOF:
            if self.current_token.type == ID:
                node = self.assign_statement()
                program_node.nodes_list.append(node)
            else:
                raise_error(self.__class__.__name__, INV_SYNTAX)
        return program_node

    def assign_statement(self):
        """assign_statement = variable ASSIGN expr"""
        var = self.variable()
        self.eat(ASSIGN)
        return AssignOp(var, self.expr())

    def expr(self):
        """expr: term (OPERATOR{'+'|'-'} term)*
           term: factor (OPERATOR{'*'|'/'} factor)*
           factor: INTEGER_CONST
                 | FLOAT_CONST
                 | L_PAREN expr R_PAREN
                 | variable"""

        node = self.term()
        while self.current_token.value in ('+', '-'):
            op_token = self.current_token
            self.eat(OPERATOR)
            node = BinOp(node, op_token, self.term())

        return node

    def term(self):
        """term: factor (OPERATOR{mult|div} factor)*"""

        node = self.factor()
        while self.current_token.value in ('*', '/'):
            op_token = self.current_token
            self.eat(OPERATOR)
            node = BinOp(node, op_token, self.factor())

        return node

    def factor(self):
        """factor: INTEGER_CONST
                 | FLOAT_CONST
                 | L_PAREN expr R_PAREN
                 | variable"""
        node = None
        token = self.current_token
        if token.type == INTEGER_CONST:
            self.eat(INTEGER_CONST)
            node = Num(token)
        elif token.type == FLOAT_CONST:
            self.eat(FLOAT_CONST)
            node = Num(token)
        elif token.type == L_PAREN:
            self.eat(L_PAREN)
            node = self.expr()
            self.eat(R_PAREN)
        elif token.type == ID:
            node = self.variable()
        else:
            raise_error(self.__class__.__name__, INV_SYNTAX)
        return node

    def variable(self):
        """variable: ID"""
        token = self.current_token
        self.eat(ID)
        return Var(token)

    def parse(self):
        return self.program()
