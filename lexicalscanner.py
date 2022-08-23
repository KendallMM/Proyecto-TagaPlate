import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID', 'NUMBER', 'ADD', 'SUB', 'MUL', 'DIV', 'MAYOR', 'MENOR', 'MAYIGUAL', 'MENIGUAL',
          'IGUAL', 'DIS', 'FUNC', 'COMMA', 'DOT', 'LPARENT', 'RPARENT', 'COMMENT']

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

t_ignore = r'\\t'
t_ID = r'@[a-zA-Z0-9]{2,9}'
t_NUMBER = r'[0-9]+'
t_ADD = r'ADD'
t_SUB = r'SUB'
t_MUL = r'MUL'
t_DIV = r'DIV'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'=='
t_DIS = r'<>'
t_MENIGUAL = r'<='
t_MAYIGUAL = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_DOT = r'\.'
t_COMMENT = r'\--.*'

def file_reader(path):
    file = open(path, mode='r')
    txt = file.read()
    file.close()
    return txt

def scanner(txt):
    x = re.findall(t_ID, txt)
    if x:
        return x
    else:
        return error_generator('variable')

def error_generator(type):
    return 'Lexical error: ' + type
    



