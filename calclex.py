import ply.lex as lex

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
)

keywords = {
    'IF',
    'THEN',
    'ENDIF',
    'FOR',
    'NEXT',
    'GOSUB',
    'RETURN'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_IF = r'if'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z]([a-zA-Z] | \d)+'
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

data = ('3 if + aAaqweqwA123 * 10\n'
        '  + -20 *2\n')

# Give the lexer some input
print(data)
lexer.input(data)

# Tokenize
for tok in lexer:
    print(tok)