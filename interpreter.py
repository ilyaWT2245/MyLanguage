from raise_error import *


class NodeVisitor(object):
    def visit(self, node):
        s = 'visit_' + node.__class__.__name__
        func = getattr(self, s, self.error_visit)
        return func(node)

    def error_visit(self, node):
        raise_error(self.__class__.__name__, VISIT_NODE)


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_Num(self, node):
        return node.value

    def visit_BinOp(self, node):
        op = node.operator
        match op:
            case '+':
                return self.visit(node.left_node) + self.visit(node.right_node)
            case '-':
                return self.visit(node.left_node) - self.visit(node.right_node)
            case '*':
                return self.visit(node.left_node) * self.visit(node.right_node)
            case '/':
                return self.visit(node.left_node) / self.visit(node.right_node)

    def interpret(self):
        tree = self.parser.parse()
        print(self.visit(tree))
