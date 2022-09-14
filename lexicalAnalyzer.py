import ply.lex as lex

err = ''

tokens = ['PRINCIPAL', 'ID', 'NUMBER', 'ADD', 'SUB', 'MUL', 'DIV', 'NEW', 'CALL', 'PROCEDURE',
          'TRUE', 'FALSE', 'NUMVAL', 'BOOLVAL', 'VALUES', 'ALTER', 'ALTERB', 'MOVR', 'MOVL',
          'HAMMER', 'STOP', 'VERT', 'REPEAT', 'UNTIL', 'WHILE', 'CASE', 'WHEN', 'THEN', 'ELSE',
          'PRINT', 'GT', 'LT', 'GET', 'LET', 'EQ', 'DT', 'COMMA', 'SEMICOLON', 'LPARENT',
          'RPARENT', 'COMMENT', 'NORTH', 'SOUTH', 'EAST', 'WEST', 'BREAK', 'STRING']

t_ignore = ' \t'
t_NUMBER = r'[0-9]+'
t_ADD = r'ADD'
t_SUB = r'SUB'
t_MUL = r'MUL'
t_DIV = r'DIV'
t_NEW = r'New'
t_CALL = r'CALL'
t_PROCEDURE = r'Proc'
t_TRUE = r'True'
t_FALSE = r'False'
t_NUMVAL = r'Num'
t_BOOLVAL = r'Bool'
t_VALUES = r'Values'
t_ALTER = r'Alter'
t_ALTERB = r'AlterB'
t_MOVR = r'MoveRight'
t_MOVL = r'MoveLeft'
t_HAMMER = r'Hammer'
t_STOP = r'Stop'
t_VERT = r'isTrue'
t_REPEAT = r'Repeat'
t_UNTIL = r'Until'
t_WHILE = r'While'
t_CASE = r'Case'
t_WHEN = r'When'
t_THEN = r'Then'
t_ELSE = r'Else'
t_BREAK = r'Break'
t_PRINT = r'PrintValues'
t_NORTH = r'N'
t_SOUTH = r'S'
t_EAST = r'E'
t_WEST = r'O'
t_GT = r'>'
t_LT = r'<'
t_GET = r'>='
t_LET = r'<='
t_EQ = r'=='
t_DT = r'<>'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_STRING = r'\".*\"'
t_COMMENT = r'--.*'

def t_ID(t):
    r'@[a-zA-Z0-9_#]{2,9}'
    if t.value == '@Principal':
        t.type = 'PRINCIPAL'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    global err
    err = "Lexical Error: Illegal character '%s' in line '%d'" % (t.value[0], t.lexer.lineno)
    t.lexer.skip(len(t.value))

def lexical_analisis(path):
    lexer = lex.lex()
    lexer.input(open(path).read())
    while True:
        token = lexer.token()
        if not token:
            lexer.lineno = 1
            break
        print(token)

