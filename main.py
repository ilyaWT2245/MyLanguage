from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    while True:
        try:
            text = input("Ввод> ")
        except EOFError:
            break
        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpr = Interpreter(parser)
        interpr.interpret()


if __name__ == '__main__':
    main()
