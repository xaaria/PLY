from ply import yacc
import lexer

# tokens are defined in lex-module, but needed here also in syntax rules
tokens = lexer.tokens



# program ::= {function_or_variable_definition} statement_list
def p_program(p):
    """
    program : program_seq statement_list
    | statement_list
    """

# Seq for p_program
def p_program_seq(p):
    """
    program_seq : function_or_variable_definition program_seq
    | function_or_variable_definition
    """

# add missing defs.
def p_function_or_variable_definition(p):
    """
    function_or_variable_definition : variable_definition
    """


def p_variable_definition(p):
    """
    variable_definition : scalar_definition
    | range_definition
    | sheet_definition
    """



# formals ::= formal_arg { COMMA formal_arg }
def p_formals(p):
    """
    formals : formal_arg formals_seq
    | formal_arg
    """

def p_formals_seq(p):
    """
    formals_seq : COMMA formal_arg formals_seq
    | COMMA formal_arg
    """


def p_formal_arg(p):
    """
    formal_arg : IDENT COLON SCALAR
    | RANGE_IDENT COLON RANGE
    | SHEET_IDENT COLON SHEET
    """


def p_sheet_definition(p):
    """
    sheet_definition : SHEET SHEET_IDENT sheet_init
    | SHEET SHEET_IDENT
    """



def p_sheet_init(p):
    """
    sheet_init : EQ sheet_init_list
    | EQ INT_LITERAL MULT INT_LITERAL
    """


# sheet_row 1-inf
def p_sheet_init_list(p):
    """
    sheet_init_list : LCURLY sheet_init_list_seq RCURLY
    """

# Seq. for above
def p_sheet_init_list_seq(p):
    """
    sheet_init_list_seq : sheet_row sheet_init_list_seq
    | sheet_row
    """



# mult. times?
def p_sheet_row(p):
    """
    sheet_row : simple_expr sheet_row_seq
    | simple_expr
    """

# Seq. see above
def p_sheet_row_seq(p):
    """
    sheet_row_seq : COMMA simple_expr sheet_row_seq
    | COMMA simple_expr
    """




def p_range_definition(p):
    """
    range_definition : RANGE RANGE_IDENT EQ range_expr
    | RANGE RANGE_IDENT
    """



def p_scalar_definition(p):
    """
    scalar_definition : SCALAR IDENT EQ scalar_expr
    | SCALAR IDENT
    """


# statement_list ::= statement { statement }
def p_statement_list(p):
    """
    statement_list : statement statement_list
    | statement
    """





def p_statement(p):
    """
    statement : PRINT_SHEET INFO_STRING SHEET_IDENT
    | PRINT_SHEET SHEET_IDENT
    | PRINT_RANGE INFO_STRING range_expr
    | PRINT_RANGE range_expr
    | PRINT_SCALAR INFO_STRING scalar_expr
    | PRINT_SCALAR scalar_expr
    | IF scalar_expr THEN statement_list ELSE statement_list ENDIF
    | IF scalar_expr THEN statement_list ENDIF
    | WHILE scalar_expr DO statement_list DONE
    | FOR range_list DO statement_list DONE
    | subroutine_call
    | RETURN scalar_expr
    | RETURN range_expr
    | assignment
    """


# mult times?
def p_range_list(p):
    """
    range_list : range_expr range_list_seq
    | range_expr
    """

def p_range_list_seq(p):
    """
    range_list_seq : COMMA range_expr range_list_seq
    | COMMA range_expr
    """


# arguments  ::= arg_expr { COMMA arg_expr }
def p_arguments(p):
    """
    arguments : arg_expr arguments_seq
    | arg_expr
    """

def p_arguments_seq(p):
    """
    arguments_seq : COMMA arg_expr arguments_seq
    | COMMA arg_expr
    """


def p_arg_expr(p):
    """
    arg_expr : scalar_expr
    | range_expr
    | SHEET_IDENT
    """


def p_subroutine_call(p):
    """
    subroutine_call : FUNC_IDENT LSQUARE arguments RSQUARE
    | FUNC_IDENT LSQUARE RSQUARE
    """


def p_assignment(p):
    """
    assignment : IDENT ASSIGN scalar_expr
    | cell_ref ASSIGN scalar_expr
    | RANGE_IDENT ASSIGN range_expr
    | SHEET_IDENT ASSIGN SHEET_IDENT
    """

def p_range_expr(p):
    """
    range_expr : RANGE_IDENT
    | RANGE cell_ref DOTDOT cell_ref
    | LSQUARE function_call RSQUARE
    | range_expr LSQUARE INT_LITERAL COMMA INT_LITERAL RSQUARE
    """

def p_cell_ref(p):
    """
    cell_ref : SHEET_IDENT SQUOTE COORDINATE_IDENT
    | DOLLAR COLON RANGE_IDENT
    | DOLLAR
    """

# scalar_expr ::= simple_expr { (EQ|NOTEQ|LT|LTEQ|GT|GTEQ) simple_expr}
def p_scalar_expr(p):
    """
    scalar_expr : simple_expr scalar_expr_seq
    | simple_expr
    """

# Seq. for above
def p_scalar_expr_seq(p):
    """
    scalar_expr_seq : EQ simple_expr scalar_expr_seq
    | NOTEQ simple_expr scalar_expr_seq
    | LT simple_expr scalar_expr_seq
    | LTEQ simple_expr scalar_expr_seq
    | GT simple_expr scalar_expr_seq
    | GTEQ simple_expr scalar_expr_seq
    | EQ simple_expr
    | NOTEQ simple_expr
    | LT simple_expr
    | LTEQ simple_expr
    | GT simple_expr
    | GTEQ simple_expr
    """



# simple_expr ::= term { (PLUS | MINUS) term }
def p_simple_expr(p):
    """
    simple_expr : term simple_expr_seq
    | term
    """

# Seq. for above
def p_simple_expr_seq(p):
    """
    simple_expr_seq : PLUS term simple_expr_seq
    | MINUS term simple_expr_seq
    | PLUS term
    | MINUS term
    """


# term ::= factor { (MULT | DIV) factor }
def p_term(p):
    """
    term : factor term_seq
    | factor
    """

# Seq for above
def p_term_seq(p):
    """
    term_seq : MULT factor term_seq
    | DIV factor term_seq
    | MULT factor
    | DIV factor
    """


def p_factor(p):
    """
    factor : MINUS atom
    | atom
    """


def p_atom(p):
    """
    atom : IDENT
    | DECIMAL_LITERAL
    | function_call
    | cell_ref
    | NUMBER_SIGN range_expr
    | LPAREN scalar_expr RPAREN
    """

def p_function_call(p):
    """
    function_call : FUNC_IDENT LSQUARE arguments RSQUARE
    | FUNC_IDENT LSQUARE RSQUARE
    """

# end of definitions



# ----------------------------------------------------------

def p_error(p):
    print('syntax error @', p)
    raise SystemExit


parser = yacc.yacc()
if __name__ == '__main__':
    import argparse, codecs
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('--who', action='store_true', help='who wrote this' )
    group.add_argument('-f', '--file', help='filename to process')
    ns = arg_parser.parse_args()

    if ns.who == True:
        # identify who wrote this
        print( "OP" )
    elif ns.file is None:
        # user didn't provide input filename
        arg_parser.print_help()
    else:
        data = codecs.open( ns.file, encoding='utf-8' ).read()
        result = parser.parse(data, lexer=lexer.lexer, debug=False)
        if result is None:
            print( 'syntax OK' )

