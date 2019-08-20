import sys
from sly import Lexer, Parser


class MyLexer(Lexer):
    tokens = {
        NUM, ID, WHILE, IF, ELSE, VOID, RETURN, INT, PLUS, MINUS, TIMES, DIVIDE, ASSIGN, EQ, LT, LE, GT, GE, NE,
        LPAREN, RPAREN,
    }
    literals = {'{', '}', ';', ',', '[', ']', '/*', '*/'}

    ignore = ' \t'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    GT = r'>'
    LT = r'<'
    GE = r'>='
    LE = r'<='
    EQ = r'=='
    NE = r'!='

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['return'] = RETURN
    ID['int'] = INT
    ID['void'] = VOID

    ignore_comment = r'[/][*][^*][*]+([^*/][^*][*]+)*[/]| '
    # ignore_comment = r'[/][*]([\w]+)*[/]'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


# class MyParser(Parser):
#
#     tokens = MyLexer.tokens
#
#     precedence = (
#         ('left', PLUS, MINUS),
#         ('left', TIMES, DIVIDE),
#         ('right', UMINUS),
#     )
#
#     @_('expr PLUS expr',
#        'expr MINUS expr',
#        'expr TIMES expr',
#        'expr DIVIDE expr')
#     def expr(self, p):
#         return ('binary-expression', p[1], p.expr0, p.expr1)
#
#     @_('LPAREN expr RPAREN')
#     def expr(self, p):
#         return ('group-expression', p.expr)
#
#     @ _('NUMBER')
#     def expr(self, p):
#         return ('number-expression', p.NUMBER)



if __name__ == "__main__":
    data = open(sys.argv[1], 'r').read()
    lexer = MyLexer()
    # parser = MyParser()
    for tok in lexer.tokenize(data):
        print(tok.type, tok.value)
