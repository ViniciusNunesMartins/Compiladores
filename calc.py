from sly import Lexer, Parser


class CalcLexer(Lexer):
    tokens = { 'ID', 'NUMBER' 'IF', 'ELSE', 'WHILE'}
    ignore = ' \t'
    op = { '=', '+', '-', '*', '/', '(', ')' }
    opr = { '==', '<', '<=', '>', '>=' '!=' }
    # Tokens

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.names = { }

    @_('ID "=" expr')
    def statement(self, p):
        self.names[p.ID] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "-" expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr "/" expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return -p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER

    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print("Undefined ID '%s'" % p.ID)
            return 0

if __name__ == '__main__':
    data = '''
    # Counting
    x = 0;
    while (x < 10) {
        print x:
        x = x + 1;
    }
    '''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(tok)