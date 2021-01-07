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
    'LESEQ',
    'MOREQ',
    'CON',
    'DEN',
    'LT',  # <
    'GT',  # >
    'EQ',  # ==
    'NE',  # /=
    'LBR',
    'LFBR',
    'RFBR',
    'RBR',
    'ASS',
    'LINEND',
    'COMMA',
] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUM(t):
    r'[0-9]+'
    if len(t.value) > 1:
        if str(t.value)[0] == '0':
            print()
            t_error(t)
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
t_LESEQ = r'(\<=)'  # <=
t_MOREQ = r'(\>=)'  # >=
t_LT = r'(\<)' # <
t_GT = r'(\>)' # >
t_EQ = r'(==)' # ==
t_NE = r'(/=)' # /=
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