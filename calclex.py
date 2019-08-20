import ply.lex as lex
import sys

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'EQUAL'
)

keywords = {
    'IF',
    'THEN',
    'ENDIF',
    'FOR',
    'NEXT',
    'RETURN'
    'INT'
    'FLOAT'
    'DOUBLE'
    'BOOLEAN'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EQUAL = R'\='
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]([a-zA-Z0-9_])+'
    t.value = str(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    # print("Illegal character '%s'," % t.value[0])
    print(t)
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = open(sys.argv[1], 'r')
lexer.input((data.read()))
for tok in lexer:
    print(tok)
