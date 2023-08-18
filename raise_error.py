INV_SYNTAX = {'en': 'Invalid syntax'}
INV_CHAR = {'en': 'Invalid character'}
IN_POS = {'en': 'in pos'}
VISIT_NODE = {'en': 'Error visiting node'}


language = 'en'


def raise_error(class_, error,
                char_pos=None, char=None):
    error_text = list()
    error_text.append(f'{class_.upper()} ERROR:')

    if error == INV_CHAR:
        error_text.append(f'{error[language]} ({char}) {IN_POS[language]} {char_pos}')
    else:
        error_text.append(f'{error}')

    print('\n'.join(error_text))
    quit()
