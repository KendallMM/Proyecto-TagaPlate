import ply.yacc as yacc
from lexicalAnalyzer import tokens
from lexicalAnalyzer import read_txt
from lexicalAnalyzer import lexer

def p_program(p):
    '''program : COMMENT bodyprogram'''
    print("program")

def p_bodyprogram1(p):
    '''bodyprogram : procedure bodyprogram'''
    print("bodyprogram1")

def p_bodyprogram2(p):
    '''bodyprogram : procedure'''
    print("bodyprogram3")

def p_bodyprogram3(p):
    '''bodyprogram : COMMENT'''

def p_bodyprogramEmpty(p):
    '''bodyprogram : empty'''
    print("bodyprogram nulo")

def p_procedure1(p):
    '''procedure : PRINCIPAL LPARENT instructions RPARENT SEMICOLON'''
    print("procedure1")

def p_procedure2(p):
    '''procedure : PROCEDURE ID LPARENT instructions RPARENT SEMICOLON'''
    print("procedure2")

def p_instructions1(p):
    '''instructions : NEW ID LPARENT datatype COMMA value RPARENT SEMICOLON instructions'''
    print("New instruction")

def p_instructions2(p):
    '''instructions : VALUES LPARENT ID COMMA value RPARENT SEMICOLON instructions'''
    print("Values instruction")
    
def p_instructions3(p):
    '''instructions : alterbody SEMICOLON instructions'''
    print("Alter instruction")

def p_instructions4(p):
    '''instructions : ALTERB LPARENT value RPARENT SEMICOLON instructions'''
    print("AlterB instruction")

def p_instructions5(p):
    '''instructions : MOVR SEMICOLON instructions'''
    print("MoveRight instruction")

def p_instructions6(p):
    '''instructions : MOVL SEMICOLON instructions'''
    print("MoveLeft instruction")

def p_instructions7(p):
    '''instructions : HAMMER LPARENT position RPARENT SEMICOLON instructions'''
    print("Hammer instruction")

def p_instructions8(p):
    '''instructions : STOP SEMICOLON instructions'''
    print("Stop instruction")

def p_instructions9(p):
    '''instructions : REPEAT LPARENT repeat_instructions RPARENT SEMICOLON instructions'''
    print("Repeat instruction")

def p_instructions10(p):
    '''instructions : untilbody SEMICOLON instructions'''
    print("Until instruction")

def p_instructions11(p):
    '''instructions : whilebody SEMICOLON instructions'''
    print("While instruction")

def p_instructions12(p):
    '''instructions : casebody SEMICOLON instructions'''
    print("Case instruction")

def p_instructions13(p):
    '''instructions : PRINT LPARENT printvalues RPARENT SEMICOLON instructions'''
    print("PrintValues instruction")

def p_instructions14(p):
    '''instructions : istrue SEMICOLON instructions'''
    print("isTrue instruction")

def p_instructions15(p):
    '''instructions : CALL LPARENT ID RPARENT SEMICOLON instructions'''
    print("Call instruction")

def p_instructions16(p):
    '''instructions : COMMENT instructions'''

def p_instructionsEmpty(p):
    '''instructions : empty'''
    print("instruccion nula")

def p_alterbody(p):
    '''alterbody : ALTER LPARENT ID COMMA operator COMMA value RPARENT'''

def p_datatype1(p):
    '''datatype : NUMVAL'''

def p_datatype2(p):
    '''datatype : BOOLVAL'''

def p_value1(p):
    '''value : NUMBER'''

def p_value2(p):
    '''value : TRUE'''

def p_value3(p):
    '''value : FALSE'''

def p_value4(p):
    '''value : alterbody'''

def p_operator1(p):
    '''operator : ADD'''

def p_operator2(p):
    '''operator : SUB'''

def p_operator3(p):
    '''operator : MUL'''

def p_operator4(p):
    '''operator : DIV'''

def p_comparator1(p):
    '''comparator : GT'''

def p_comparator2(p):
    '''comparator : LT'''

def p_comparator3(p):
    '''comparator : GET'''

def p_comparator4(p):
    '''comparator : LET'''

def p_comparator5(p):
    '''comparator : EQ'''

def p_comparator6(p):
    '''comparator : DT'''

def p_position1(p):
    '''position : NORTH'''

def p_position2(p):
    '''position : SOUTH'''

def p_position3(p):
    '''position : EAST'''

def p_position4(p):
    '''position : WEST'''

def p_repeatInstructions(p):
    '''repeat_instructions : instructions BREAK'''

def p_untilbody(p):
    '''untilbody : UNTIL LPARENT instructions RPARENT condition'''

def p_whilebody(p):
    '''whilebody : WHILE condition LPARENT instructions RPARENT'''

def p_casebody1(p):
    '''casebody : CASE WHEN LPARENT condition RPARENT THEN LPARENT instructions RPARENT'''

def p_casebody2(p):
    '''casebody : casebody ELSE LPARENT instructions RPARENT'''

def p_casebody3(p):
    '''casebody : CASE ID innercasebody'''

def p_innercasebody1(p):
    '''innercasebody : WHEN NUMBER THEN LPARENT instructions RPARENT innercasebody'''

def p_innercasebody2(p):
    '''innercasebody : WHEN TRUE THEN LPARENT instructions RPARENT innercasebody'''

def p_innercasebody3(p):
    '''innercasebody : WHEN FALSE THEN LPARENT instructions RPARENT innercasebody'''

def p_innercasebodyEmpty(p):
    '''innercasebody : empty'''
    print("nulo")
    
def p_condition1(p):
    '''condition : ID comparator ID'''

def p_condition2(p):
    '''condition : ID comparator NUMBER'''

def p_condition3(p):
    '''condition : NUMBER comparator ID'''

def p_condition4(p):
    '''condition : NUMBER comparator NUMBER'''

def p_condition5(p):
    '''condition : TRUE'''

def p_condition6(p):
    '''condition : FALSE'''

def p_condition7(p):
    '''condition : istrue'''

def p_istrue(p):
    '''istrue : VERT LPARENT ID RPARENT'''

def p_printvalues1(p):
    '''printvalues : STRING printvalues'''

def p_printvalues2(p):
    '''printvalues : COMMA ID printvalues'''

def p_printvaluesEmpty(p):
    '''printvalues : empty'''
    print("printvalues nulo")
    
def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p.type != 'COMMENT' and p.lineno == 1:
        print("Sintax error on line 1: Missing expected initial comment.")
    else:
        print("Sintax error on line %d: %s does not match %s position." % (p.lineno, p.value, p.type))

txt = read_txt('prueba.txt')
parser = yacc.yacc()
result = parser.parse(txt)
print(result)
