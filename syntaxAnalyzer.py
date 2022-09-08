import ply.yacc as yacc
from lexicalAnalyzer import tokens
from parseTree import *

err = ''
errorCounter=0

def p_program(p):
    '''program : COMMENT bodyprogram'''
    #p[0] = Program(p[1], p[2], 'Program')

def p_bodyprogram1(p):
    '''bodyprogram : procedure bodyprogram'''
    #p[0] = BodyProgram1(p[1], p[2], 'BodyProgram1')

def p_bodyprogram2(p):
    '''bodyprogram : procedure'''
    #p[0] = BodyProgram2(p[1], 'BodyProgram2')

def p_bodyprogram3(p):
    '''bodyprogram : COMMENT'''
    #p[0] = BodyProgram3(p[1], 'BodyProgram3')

def p_bodyprogramEmpty(p):
    '''bodyprogram : empty'''
    #p[0] = NullNode()

def p_procedure1(p):
    '''procedure : PRINCIPAL LPARENT instructions RPARENT SEMICOLON'''
    #p[0] = Procedure1(p[1], p[2],p[3], p[4],p[5], 'Procedure1')

def p_procedure2(p):
    '''procedure : PROCEDURE ID LPARENT instructions RPARENT SEMICOLON'''
    #p[0] = Procedure2(p[1], p[2],p[3], p[4],p[5],p[6], 'Procedure2')

def p_instructions1(p):
    '''instructions : NEW ID LPARENT datatype COMMA value RPARENT SEMICOLON instructions'''
    #p[0] = Instructions1(p[1], p[2],p[3], p[4],p[5],p[6],p[7],p[8],p[9], 'Instructions1')

def p_instructions2(p):
    '''instructions : VALUES LPARENT ID COMMA value RPARENT SEMICOLON instructions'''
    #p[0] = Instructions2(p[1], p[2],p[3], p[4],p[5],p[6],p[7],p[8], 'Instructions2')
    
def p_instructions3(p):
    '''instructions : ALTER LPARENT ID COMMA operator COMMA value RPARENT SEMICOLON instructions'''
    #p[0] = Instructions3(p[1], p[2],p[3], p[4],p[5],p[6],p[7],p[8],p[9],p[10], 'Instructions3')

def p_instructions4(p):
    '''instructions : ALTERB LPARENT value RPARENT SEMICOLON instructions'''
    #p[0] = Instructions4(p[1], p[2],p[3], p[4],p[5],p[6], 'Instructions4')

def p_instructions5(p):
    '''instructions : MOVR SEMICOLON instructions'''
    #p[0] = Instructions5(p[1], p[2],p[3], 'Instructions5')

def p_instructions6(p):
    '''instructions : MOVL SEMICOLON instructions'''
    #p[0] = Instructions6(p[1], p[2],p[3], 'Instructions6')

def p_instructions7(p):
    '''instructions : HAMMER LPARENT position RPARENT SEMICOLON instructions'''
    #p[0] = Instructions7(p[1], p[2], p[3], p[4], p[5], p[6], 'Instructions7')

def p_instructions8(p):
    '''instructions : STOP SEMICOLON instructions'''
    #p[0] = Instructions8(p[1], p[2], p[3], 'Instructions8')

def p_instructions9(p):
    '''instructions : REPEAT LPARENT repeat_instructions RPARENT SEMICOLON instructions'''
    #p[0] = Instructions9(p[1], p[2], p[3], p[4], p[5], p[6], 'Instructions9')

def p_instructions10(p):
    '''instructions : untilbody SEMICOLON instructions'''
    #p[0] = Instructions10(p[1], p[2], p[3], 'Instructions10')

def p_instructions11(p):
    '''instructions : whilebody SEMICOLON instructions'''
    #p[0] = Instructions11(p[1], p[2], p[3], 'Instructions11')

def p_instructions12(p):
    '''instructions : casebody SEMICOLON instructions'''
    #p[0] = Instructions12(p[1], p[2], p[3], 'Instructions12')

def p_instructions13(p):
    '''instructions : PRINT LPARENT printvalues RPARENT SEMICOLON instructions'''
    #p[0] = Instructions13(p[1], p[2], p[3], p[4], p[5], p[6], 'Instructions13')

def p_instructions14(p):
    '''instructions : istrue SEMICOLON instructions'''
    #p[0] = Instructions14(p[1], p[2], p[3], 'Instructions14')

def p_instructions15(p):
    '''instructions : CALL LPARENT ID RPARENT SEMICOLON instructions'''
    #p[0] = Instructions15(p[1], p[2], p[3], p[4], p[5], p[6], 'Instructions15')

def p_instructions16(p):
    '''instructions : COMMENT instructions'''
    #p[0] = Instructions16(p[1], p[2], 'Instructions16')

def p_instructionsEmpty(p):
    '''instructions : empty'''
    print("instruccion nula")

def p_datatype1(p):
    '''datatype : NUMVAL'''
    #p[0] = DataType1(p[1], 'DataType1')
def p_datatype2(p):
    '''datatype : BOOLVAL'''
    #p[0] = DataType2(p[1], 'DataType2')
def p_value1(p):
    '''value : NUMBER'''
    #p[0] = Value1(p[1], 'Value1')
def p_value2(p):
    '''value : TRUE'''
    #p[0] = Value2(p[1], 'Value2')
def p_value3(p):
    '''value : FALSE'''
    #p[0] = Value3(p[1], 'Value3')
def p_value4(p):
    '''value : ALTER LPARENT ID COMMA operator COMMA value RPARENT'''
    #p[0] = Value4(p[1],p[2],p[3], p[4],p[5],p[6],p[7],p[8], 'Value4')
def p_operator1(p):
    '''operator : ADD'''
    #p[0] = Operator1(p[1], 'Operator1')
def p_operator2(p):
    '''operator : SUB'''
    #p[0] = Operator2(p[1], 'Operator2')
def p_operator3(p):
    '''operator : MUL'''
    #p[0] = Operator3(p[1], 'Operator3')
def p_operator4(p):
    '''operator : DIV'''
    #p[0] = Operator4(p[1], 'Operator4')
def p_comparator1(p):
    '''comparator : GT'''
    #p[0] = Comparator1(p[1], 'Comparator1')
def p_comparator2(p):
    '''comparator : LT'''
    #p[0] = Comparator2(p[1], 'Comparator2')
def p_comparator3(p):
    '''comparator : GET'''
    #p[0] = Comparator3(p[1], 'Comparator3')
def p_comparator4(p):
    '''comparator : LET'''
    #p[0] = Comparator4(p[1], 'Comparator4')
def p_comparator5(p):
    '''comparator : EQ'''
    #p[0] = Comparator5(p[1], 'Comparator5')
def p_comparator6(p):
    '''comparator : DT'''
    #p[0] = Comparator6(p[1], 'Comparator6')
def p_position1(p):
    '''position : NORTH'''
    #p[0] = Position1(p[1], 'Position1')
def p_position2(p):
    '''position : SOUTH'''
    #p[0] = Position2(p[1], 'Position2')
def p_position3(p):
    '''position : EAST'''
    #p[0] = Position3(p[1], 'Position3')
def p_position4(p):
    '''position : WEST'''
    #p[0] = Position4(p[1], 'Position4')
def p_repeatInstructions(p):
    '''repeat_instructions : instructions BREAK'''
    #p[0] = RepeatInstructions(p[1], p[2], 'RepeatInstructions')
def p_untilbody(p):
    '''untilbody : UNTIL LPARENT instructions RPARENT condition'''
    #p[0] = UntilBody(p[1], p[2],p[3], p[4],p[5], 'UntilBody')
def p_whilebody(p):
    '''whilebody : WHILE condition LPARENT instructions RPARENT'''
    #p[0] = WhileBody(p[1], p[2],p[3], p[4],p[5], 'WhileBody')
def p_casebody1(p):
    '''casebody : CASE WHEN LPARENT condition RPARENT THEN LPARENT instructions RPARENT'''
    #p[0] = CaseBody1(p[1],p[2],p[3], p[4],p[5],p[6],p[7],p[8],p[9], 'CaseBody1')
def p_casebody2(p):
    '''casebody : casebody ELSE LPARENT instructions RPARENT'''
    #p[0] = CaseBody2(p[1],p[2],p[3], p[4],p[5], 'CaseBody2')
def p_casebody3(p):
    '''casebody : CASE ID innercasebody'''
    #p[0] = CaseBody3(p[1],p[2],p[3], 'CaseBody3')
def p_innercasebody1(p):
    '''innercasebody : WHEN NUMBER THEN LPARENT instructions RPARENT innercasebody'''
    #p[0] = InnerCaseBody1(p[1],p[2],p[3], p[4],p[5],p[6],p[7], 'InnerCaseBody1')
def p_innercasebody2(p):
    '''innercasebody : WHEN TRUE THEN LPARENT instructions RPARENT innercasebody'''
    #p[0] = InnerCaseBody2(p[1],p[2],p[3], p[4],p[5],p[6],p[7], 'InnerCaseBody2')
def p_innercasebody3(p):
    '''innercasebody : WHEN FALSE THEN LPARENT instructions RPARENT innercasebody'''
    #p[0] = InnerCaseBody3(p[1],p[2],p[3], p[4],p[5],p[6],p[7], 'InnerCaseBody3')
def p_innercasebodyEmpty(p):
    '''innercasebody : empty'''
    print("nulo")
    #p[0] = InnerCaseBodyEmpty(p[1], 'InnerCaseBodyEmpty')
def p_condition1(p):
    '''condition : ID comparator ID'''
    #p[0] = Condition1(p[1],p[2],p[3], 'Condition1')
def p_condition2(p):
    '''condition : ID comparator NUMBER'''
    #p[0] = Condition2(p[1],p[2],p[3], 'Condition2')
def p_condition3(p):
    '''condition : NUMBER comparator ID'''
    #p[0] = Condition3(p[1],p[2],p[3], 'Condition3')
def p_condition4(p):
    '''condition : NUMBER comparator NUMBER'''
    #p[0] = Condition4(p[1],p[2],p[3], 'Condition4')
def p_condition5(p):
    '''condition : TRUE'''
    #p[0] = Condition5(p[1], 'Condition5')
def p_condition6(p):
    '''condition : FALSE'''
    #p[0] = Condition6(p[1], 'Condition6')
def p_condition7(p):
    '''condition : istrue'''
    #p[0] = Condition7(p[1], 'Condition7')
def p_istrue(p):
    '''istrue : VERT LPARENT ID RPARENT'''
    #p[0] = IsTrue(p[1],p[2],p[3],p[4], 'IsTrue')
def p_printvalues1(p):
    '''printvalues : STRING printvalues'''
    #p[0] = PrintValues1(p[1],p[2], 'PrintValues1')
def p_printvalues2(p):
    '''printvalues : COMMA ID printvalues'''
    #p[0] = PrintValues2(p[1],p[2],p[3], 'PrintValues2')
def p_printvaluesEmpty(p):
    '''printvalues : empty'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    global err
    global errorCounter
    errorCounter+1
    if p.type:
        if p.type != 'COMMENT' and p.lineno == 1:
            err = "Sintax error on line 1: Missing expected initial comment."
        else:
            err = "Sintax error on line %d: %s does not match %s position." % (p.lineno, p.value, p.type)

def sintax_analisis(path):
    global errorCounter
    parser = yacc.yacc()
    result = parser.parse(open(path).read())
    #result.imprimir(" ")
    #print(result.traducir())
    #graphFile = open('graphtree','w')
    #graphFile.write(result.traducir())
    #graphFile.close()
    print(result)
    if (errorCounter==0):
        errorCounter=-1


