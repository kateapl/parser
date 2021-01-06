import ply.lex as lex
import re

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
    'return': 'RETURN',
    'while': 'WHILE'
}

tokens = [
    'NUM',
    'PLUS',
    'DEG',
    'MUL',
    'MINUS',
    'DIVIDE',
    'ID',
    'DIS',
    'CON',
    'DEN',
    'COMPAR',
    'LBR',
    'LFBR',
    'RFBR',
    'RBR',
    'ASS',
    'LINEND',
    'COMMA',
] + list(reserved.values())


def t_ID(t):
    r'[a-z_][a-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


t_PLUS = r'\+'
t_MUL = r'\*'
t_LBR = r'\('
t_RBR = r'\)'
t_LFBR = r'\{'
t_RFBR = r'\}'
t_MINUS = r'\-'
t_DEG = r'\*\*'  # **
t_DIVIDE = r'/'
t_DIS = r'\|\|'  # ||
t_CON = r'&&'
t_DEN = r'\-\-'
t_COMPAR = r'(\<|\<=|==|\>|\>=|/=)'  # <, <=, ==, /=, >, >=
t_ASS = r'='
t_LINEND = r';'
t_COMMA = r','

t_ignore = ' \t\n'


# def t_newline(t):
    # r';'
    # t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character ", t.value[0])
    raise SystemExit(2)


lexer = lex.lex()

read_file = open('input.txt', 'r')
text = read_file.read()
read_file.close()
lexer.input(text)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)