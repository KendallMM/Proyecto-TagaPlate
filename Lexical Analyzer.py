import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'NUMBER', 'ADD', 'SUB', 'MUL', 'DIV', 'GT', 'LT', 'GET', 'LET',
          'EQUAL', 'DT', 'FUNC', 'COMMA', 'DOT', 'LPARENT', 'RPARENT', 'COMMENT']

keywords = {'New': 'NEW',
            'CALL': 'CALL',
            'Proc': 'PROCEDURE',
            '@Principal': 'PRIN',
            'True': 'TRUE',
            'False': 'FALSE',
            'Num': 'NUMVAL',
            'Bool': 'BOOLVAL',
            'Values': 'VALUES',
            'Alter': 'ALTERA',
            'AlterB': 'ALTERB',
            'MoveRight': 'MOVR',
            'MoveLeft': 'MOVL',
            'Hammer': 'HAMM',
            'Stop': 'STOP',
            'isTrue': 'VERT',
            'Repeat': 'REPEAT',
            'Until': 'UNTIL',
            'While': 'WHILE',
            'Case': 'CASE',
            'When': 'WHEN',
            'Then': 'THEN',
            'Else': 'ELSE',
            'PrintValues': 'PRINT'}

tokens = tokens + list(keywords.values())

t_ignore = '\t'
t_SUMA = 'ADD'
t_RESTA = 'SUB'
t_MULTIPLICACION = 'MUL'
t_DIVISION = 'DIV'
t_MAYOR = '>'
t_MENOR = '<'
t_IGUAL = '=='
t_DISTINTO = '<>'
t_MENIGUAL = '<='
t_MAYIGUAL = '>='

def t_ID(t):
    r'@[a-zA-Z_][a-zA-Z0-9_]*'
def t_COMENTARIOS(t):
    r'\--.*'
    pass



