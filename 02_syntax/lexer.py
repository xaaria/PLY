import ply.lex as lex
from decimal import *

# OP - 2020

# Token object has attributes tok.type, tok.value, tok.lineno, and tok.lexpos
# For example LexToken(COMMENT,'...foo...',1,0)

reserved = {
  'if': 'IF',
  'endif': 'ENDIF',
  'then': 'THEN',
  'else': 'ELSE',
  'end': 'END',
  'while': 'WHILE',
  'for': 'FOR',
  'return': 'RETURN',
  'function': 'FUNCTION',
  'subroutine': 'SUBROUTINE',
  'is': 'IS',
  'range': 'RANGE',
  'sheet': 'SHEET',
  'scalar': 'SCALAR',
  'do': 'DO',
  'done': 'DONE',
  'print_sheet': 'PRINT_SHEET',
  'print_scalar': 'PRINT_SCALAR',
  'print_range': 'PRINT_RANGE',
}



# "All lexers must provide a list tokens that defines all of the possible token names that can be produced by the lexer"
tokens = [
  'PLUS', 'MINUS', 'DIV', 'MULT', 'LPAREN', 'RPAREN',
  'ASSIGN', 'LSQUARE', 'RSQUARE', 'LCURLY', 'RCURLY',
  'COMMA', 'DOTDOT', 'SQUOTE', 'COLON', 'DOLLAR', 'NUMBER_SIGN',
  'EQ', 'NOTEQ', 'LT', 'LTEQ', 'GT', 'GTEQ',
  'INT_LITERAL', 'DECIMAL_LITERAL', 'IDENT', 'COORDINATE_IDENT', 'RANGE_IDENT',
  'INFO_STRING', 'SHEET_IDENT', 'FUNC_IDENT'
] + list(reserved.values())

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'
t_DIV     = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LCURLY  = r'\{'
t_RCURLY  = r'\}'

t_ASSIGN = r'\:='   # !!!

t_COMMA  = r'\,'
t_DOTDOT = r'\..'
t_SQUOTE = r"\'"
t_COLON  = r'\:'
t_DOLLAR = r'\$'
t_NUMBER_SIGN = r'\#'

t_NOTEQ = r'\!='
t_EQ    = r'\='
t_LTEQ  = r'\<='
t_LT    = r'\<'
t_GTEQ  = r'\>='
t_GT    = r'\>'

# Ignored characters
t_ignore = " \t"  # space and tab



# Checks for reserved words. Try to find from reserved dict. Reserved are lowercase
# Every token that looks like (matches) reserved word, but is not, is an IDENT if len >= 2
# Not going to explain why it is done like this, you can try it yourself and see...
def t_RESERVED_OR_IDENT(t):
  r'[a-z]+[a-z_]*'
  if t.value in reserved.keys():
    t.type = t.value.upper()
    return t

  elif len(t.value) >= 2:

    t.type = "IDENT"
    return t

  else:
    pass


# token definitions:

def t_COMMENT(t):
  r'\.\.\.{1}.*\.\.\.{1}' # or \.\.\.{1}\.\.\.{1}
  #return t
  pass

# Notice: also empty comment str allowed: "!!" ==> ''
def t_INFO_STRING(t):
  r'!{1}.*!{1}'
  t.value = str(t.value[1:-1]) # omit ! from end and beginning
  return t

# COORDINATE or COORD?

def t_COORDINATE_IDENT(t):
  r'[A-Z]{1,2}\d{1,3}'
  return t

def t_DECIMAL_LITERAL(t):
  r'-?\d+\.\d{1}'
  t.value = Decimal(t.value)
  return t

def t_INT_LITERAL(t):
  r'-?\d+'
  t.value = int(t.value)
  return t


def t_RANGE_IDENT(t):
  r'_+[A-Za-z0-9_]+'
  return t



# starts with an uppercase letter (A-Z) and must be followed by at least one character in et( 'a-z', '0-9', '_' )
def t_FUNC_IDENT(t):
  r'[A-Z][a-z0-9_]+'
  return t

def t_SHEET_IDENT(t):
  r'[A-Z]+'
  return t

"""
# Never evaluated because reserved word -check also matches this...
def t_IDENT(t):
  r'[a-z]{1}[A-Za-z0-9_]+'
  return t
"""

# Meta functions:

def t_error(t):
  raise Exception("Illegal character '{}' at line {}".format(t.value[0], t.lexer.lineno))

def t_newline(t):
  r'\n+'
  t.lexer.lineno += t.value.count("\n")




lexer = lex.lex()

if __name__ == '__main__':

  import argparse, codecs
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  group.add_argument('--who', action='store_true', help='who wrote this')
  group.add_argument('-f', '--file', help='filename to process')

  ns = parser.parse_args()
  if ns.who == True:
    print( 'OP' )
  elif ns.file is None:
    # user didn't provide input filename
    parser.print_help()
  else:

    with codecs.open( ns.file, 'r', encoding='utf-8' ) as INFILE:
      data = INFILE.read()
      lexer.input( data )

      while True:
        token = lexer.token()
        if token is None:
          break

        print(token)
