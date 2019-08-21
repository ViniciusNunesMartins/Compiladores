import sys
import MyLexer


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
    lexer = MyLexer.MyLexer()
    l = list()
    for tok in lexer.tokenize(data):
        l.append(tok.value)

    print(l)
