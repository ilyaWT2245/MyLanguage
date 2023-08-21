from raise_error import *


class NodeVisitor(object):
    def visit(self, node):
        s = 'visit_' + type(node).__name__
        func = getattr(self, s, self.error_visit)
        return func(node)

    def error_visit(self, node):
        raise_error(self.__class__.__name__, VISIT_NODE)


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.GLOBAL_SCOPE = {}
        self.parser = parser

    def visit_Program(self, node):
        for n in node.nodes_list:
            self.visit(n)

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

    def visit_AssignOp(self, node):
        name = node.var_node.value
        value = self.visit(node.right_node)
        self.GLOBAL_SCOPE[name] = value

    def visit_Var(self, node):
        value = self.GLOBAL_SCOPE.get(node.value, None)
        if value is None:
            raise_error(self.__class__.__name__, VAR_DECL,
                        variable=node.value)
        else:
            return value

    def interpret(self):
        tree = self.parser.parse()
        self.visit(tree)
