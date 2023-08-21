from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def main():
    while True:
        try:
            name = input("Укажите директорию файла> ")
            try:
                file = open(name)
            except FileNotFoundError:
                print('File not found')
                continue
        except EOFError:
            break
        text = file.read()
        file.close()

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        interpreter.interpret()
        print('GLOBAL SCOPE:')
        for key, value in interpreter.GLOBAL_SCOPE.items():
            print(f' {key}: {value}')


if __name__ == '__main__':
    main()
