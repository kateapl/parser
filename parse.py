import ply.yacc as yacc

from lex import tokens


class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts


def p_program(p):
    '''program : progbody func'''
    p[0] = Node('program', [p[1], p[2]])


def p_progbody(p):
    '''progbody :
                | progbody func'''
    if len(p) > 1:
        if p[1] is None:
            p[1] = Node('body', [])
        p[0] = p[1].add_parts([p[2]])


def p_func(p):
    '''func : DEF ID LBR args RBR LFBR funcbody RFBR'''
    p[0] = Node(p[2], [p[4], p[7]])


def p_args(p):
    '''args :
            | ID
            | args COMMA ID'''
    if len(p) == 1:
        p[0] = Node('args', [])
    elif len(p) == 2:
        p[0] = Node('args', [p[1]])
    else:
        p[0] = p[1].add_parts([p[3]])


def p_funcbody(p):
    '''funcbody :
                | if funcbody
                | funcall funcbody
                | assign funcbody
                | while funcbody
                | return funcbody'''
    if len(p) == 1:
        p[0] = Node('funcbody', [])
    else:
        p[0] = p[2].add_parts([p[1]])


def p_assign(p):
    '''assign : ID ASS expression LINEND
              | ID ASS funcall'''
    p[0] = Node('assign', [p[1], p[3]])


def p_funcall(p):
    '''funcall : ID LBR args RBR LINEND'''
    p[0] = Node('call func '+p[1], [p[3]])


def p_if(p):
    '''if : IF LBR expression RBR LFBR funcbody RFBR ELSE LFBR funcbody RFBR
          | IF LBR expression RBR LFBR funcbody RFBR'''
    if len(p) == 12:
        p[0] = Node('if', [p[3], p[6]]) if p[2] != 0 else Node('else', [p[3], p[10]])
    else:
        p[0] = Node('if', [p[3], p[6]]) if p[2] != 0 else None


def p_while(p):
    '''while : WHILE LBR expression RBR LFBR funcbody RFBR'''
    if p[3] != 0:
        p[0] = Node('while', [p[3], p[6]])


def p_return(p):
    '''return : RETURN expression LINEND
              | RETURN ID LINEND '''
    p[0] = Node('return', p[2])


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = Node(p[2], [p[1], p[3]])


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = Node(p[2], [p[1], p[3]])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term MUL factor'
    p[0] = Node(p[2], [p[1], p[3]])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = Node(p[2], [p[1], p[3]])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LBR expression RBR'
    p[0] = p[2]


def p_error(p):
    print("parser ")
    print("Unexpected token:", p)


parser = yacc.yacc()


def build_tree(text):
    print('------text----------')
    print(text)
    print('------text----------')
    return parser.parse(text)


def outputing():
    read_file = open('input.txt', 'r')
    text = read_file.read()
    result = build_tree(text)
    print('------res----------')
    print(result)
    print('------res----------')

    write_file = open('output.txt', 'w')
    write_file.write(result)