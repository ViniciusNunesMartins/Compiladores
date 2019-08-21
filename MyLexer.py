from sly import Lexer
from sly import Parser

class MyLexer(Lexer):
    tokens = {
        'NUM', 'ID', 'WHILE', 'IF', 'ELSE', 'VOID', 'RETURN', 'INT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'EQ', 'LT', 'LE', 'GT', 'GE', 'NE',
        'LPAREN', 'RPAREN',
    }
    literals = {'{', '}', ';', ',', '[', ']', '/*', '*/'}
    # ignore_comment = r'[\/][*][^*]*[*]+([^*\/][^*]*[*]+)*[\/]'
    ignore = ' \t'

    @_(r'[\/][*][^*]*[*]+([^*\/][^*]*[*]+)*[\/]')
    def ignore_comment(self, p):
        self.lineno += len(p.value.split('\n')) - 1

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

    @_(r'[0-9]+')
    def NUM(self, t):
        t.value = int(t.value)
        return t

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = 'IF'
    ID['else'] = 'ELSE'
    ID['while'] = 'WHILE'
    ID['return'] = 'RETURN'
    ID['int'] = 'INT'
    ID['void'] = 'VOID'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1