INV_SYNTAX = {'en': 'Invalid syntax'}
INV_CHAR = {'en': 'Invalid character'}
IN_POS = {'en': 'in pos'}
VISIT_NODE = {'en': 'Error visiting node'}
VAR_DECL = {'en': 'Variable'}
NOT_FOUND = {'en': 'is not found'}


language = 'en'


def raise_error(class_, error,
                char_pos=None, char=None,
                variable=None):
    error_text = list()
    error_text.append(f'{class_.upper()} ERROR:')

    if error == INV_CHAR:
        error_text.append(f'{error[language]} ({char}) {IN_POS[language]} {char_pos}')
    elif error == VAR_DECL:
        error_text.append(f'{VAR_DECL[language]} {variable} {NOT_FOUND[language]}')
    else:
        error_text.append(f'{error[language]}')

    print('\n'.join(error_text))
    quit()
