import ply.yacc as yacc
from LexicalAnalyzer import tokens
from ParseTree import *

err = ''
errorCounter = 0
root = None


def p_program(p):
    '''program : COMMENT procedures principal procedures'''
    p[0] = Program(p[1], p[2], p[3], p[4], 'Program')
    global root
    root = p[0]


def p_principal(p):
    '''principal : PRINCIPAL LPARENT instructions RPARENT SEMICOLON'''
    p[0] = Principal(p[1], p[2], p[3], p[4], p[5], 'Principal')


def p_principalEmpty(p):
    '''principal : empty'''
    global err, errorCounter
    err = "Syntax error: Principal method not found."
    errorCounter = errorCounter + 2
    p[0] = NullNode()


def p_procedures(p):
    '''procedures : PROCEDURE ID LPARENT instructions RPARENT SEMICOLON procedures'''
    p[0] = Procedures(p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'Procedure')


def p_proceduresEmpty(p):
    '''procedures : empty'''
    p[0] = NullNode()


def p_instructions1(p):
    '''instructions : instructions NEW ID LPARENT datatype COMMA value RPARENT SEMICOLON commentary'''
    p[0] = Instructions1(p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[1], 'Instructions1')


def p_instructions2(p):
    '''instructions : instructions VALUES LPARENT ID COMMA value RPARENT SEMICOLON commentary'''
    p[0] = Instructions2(p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[1], 'Instructions2')


def p_instructions3(p):
    '''instructions : instructions ALTER LPARENT ID COMMA operator COMMA value RPARENT SEMICOLON commentary'''
    p[0] = Instructions3(p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[1], 'Instructions3')


def p_instructions4(p):
    '''instructions : instructions ALTERB LPARENT ID RPARENT SEMICOLON commentary'''
    p[0] = Instructions4(p[2], p[3], p[4], p[5], p[6], p[7], p[1], 'Instructions4')


def p_instructions5(p):
    '''instructions : instructions MOVR SEMICOLON commentary'''
    p[0] = Instructions5(p[2], p[3], p[4], p[1], 'Instructions5')


def p_instructions6(p):
    '''instructions : instructions MOVL SEMICOLON commentary'''
    p[0] = Instructions6(p[2], p[3], p[4], p[1], 'Instructions6')


def p_instructions7(p):
    '''instructions : instructions HAMMER LPARENT position RPARENT SEMICOLON commentary'''
    p[0] = Instructions7(p[2], p[3], p[4], p[5], p[6], p[7], p[1], 'Instructions7')


def p_instructions8(p):
    '''instructions : instructions STOP SEMICOLON commentary'''
    p[0] = Instructions8(p[2], p[3], p[4], p[1], 'Instructions8')


def p_instructions9(p):
    '''instructions : instructions REPEAT LPARENT repeat_instructions RPARENT SEMICOLON commentary'''
    p[0] = Instructions9(p[2], p[3], p[4], p[5], p[6], p[7], p[1], 'Instructions9')


def p_instructions10(p):
    '''instructions : instructions untilbody SEMICOLON commentary'''
    p[0] = Instructions10(p[2], p[3], p[4], p[1], 'Instructions10')


def p_instructions11(p):
    '''instructions : instructions whilebody SEMICOLON commentary'''
    p[0] = Instructions11(p[2], p[3], p[4], p[1], 'Instructions11')


def p_instructions12(p):
    '''instructions : instructions casebody SEMICOLON commentary'''
    p[0] = Instructions12(p[2], p[3], p[4], p[1], 'Instructions12')


def p_instructions13(p):
    '''instructions : instructions PRINT LPARENT printstart RPARENT SEMICOLON commentary'''
    p[0] = Instructions13(p[2], p[3], p[4], p[5], p[6], p[7], p[1], 'Instructions13')


def p_instructions14(p):
    '''instructions : instructions istrue SEMICOLON commentary'''
    p[0] = Instructions14(p[2], p[3], p[4], p[1], 'Instructions14')


def p_instructions15(p):
    '''instructions : instructions CALL LPARENT ID RPARENT SEMICOLON commentary'''
    p[0] = Instructions15(p[2], p[3], p[4], p[5], p[6], p[7], p[1], 'Instructions15')


def p_instructionsEmpty(p):
    '''instructions : empty'''
    p[0] = NullNode()


def p_commentary1(p):
    '''commentary : COMMENT'''
    p[0] = Commentary1(p[1], 'Commentary1')

def p_commentary2(p):
    '''commentary : empty'''
    p[0] = NullNode()

def p_datatype1(p):
    '''datatype : NUMVAL'''
    p[0] = DataType1(p[1], 'DataType1')


def p_datatype2(p):
    '''datatype : BOOLVAL'''
    p[0] = DataType2(p[1], 'DataType2')


def p_value1(p):
    '''value : NUMBER'''
    p[0] = Value1(p[1], 'Value1')


def p_value2(p):
    '''value : TRUE'''
    p[0] = Value2(p[1], 'Value2')


def p_value3(p):
    '''value : FALSE'''
    p[0] = Value3(p[1], 'Value3')


def p_value4(p):
    '''value : ALTER LPARENT ID COMMA operator COMMA value RPARENT'''
    p[0] = Value4(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], 'Value4')


def p_operator1(p):
    '''operator : ADD'''
    p[0] = Operator1(p[1], 'Operator1')


def p_operator2(p):
    '''operator : SUB'''
    p[0] = Operator2(p[1], 'Operator2')


def p_operator3(p):
    '''operator : MUL'''
    p[0] = Operator3(p[1], 'Operator3')


def p_operator4(p):
    '''operator : DIV'''
    p[0] = Operator4(p[1], 'Operator4')


def p_comparator1(p):
    '''comparator : GT'''
    p[0] = Comparator1(p[1], 'Comparator1')


def p_comparator2(p):
    '''comparator : LT'''
    p[0] = Comparator2(p[1], 'Comparator2')


def p_comparator3(p):
    '''comparator : GET'''
    p[0] = Comparator3(p[1], 'Comparator3')


def p_comparator4(p):
    '''comparator : LET'''
    p[0] = Comparator4(p[1], 'Comparator4')


def p_comparator5(p):
    '''comparator : EQ'''
    p[0] = Comparator5(p[1], 'Comparator5')


def p_comparator6(p):
    '''comparator : DT'''
    p[0] = Comparator6(p[1], 'Comparator6')


def p_position1(p):
    '''position : NORTH'''
    p[0] = Position1(p[1], 'Position1')


def p_position2(p):
    '''position : SOUTH'''
    p[0] = Position2(p[1], 'Position2')


def p_position3(p):
    '''position : EAST'''
    p[0] = Position3(p[1], 'Position3')


def p_position4(p):
    '''position : WEST'''
    p[0] = Position4(p[1], 'Position4')


def p_repeatInstructions(p):
    '''repeat_instructions : instructions BREAK'''
    p[0] = RepeatInstructions(p[1], p[2], 'RepeatInstructions')


def p_untilbody(p):
    '''untilbody : UNTIL LPARENT instructions RPARENT condition'''
    p[0] = UntilBody(p[1], p[2], p[3], p[4], p[5], 'UntilBody')


def p_whilebody(p):
    '''whilebody : WHILE condition LPARENT instructions RPARENT'''
    p[0] = WhileBody(p[1], p[2], p[3], p[4], p[5], 'WhileBody')


def p_casebody1(p):
    '''casebody : CASE WHEN LPARENT condition RPARENT THEN LPARENT instructions RPARENT'''
    p[0] = CaseBody1(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], 'CaseBody1')


def p_casebody2(p):
    '''casebody : casebody ELSE LPARENT instructions RPARENT'''
    p[0] = CaseBody2(p[1], p[2], p[3], p[4], p[5], 'CaseBody2')


def p_casebody3(p):
    '''casebody : CASE ID innercasebody'''
    p[0] = CaseBody3(p[1], p[2], p[3], 'CaseBody3')


def p_innercasebody1(p):
    '''innercasebody : WHEN NUMBER THEN LPARENT instructions RPARENT innercasebody'''
    p[0] = InnerCaseBody1(p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'InnerCaseBody1')


def p_innercasebody2(p):
    '''innercasebody : WHEN TRUE THEN LPARENT instructions RPARENT innercasebody'''
    p[0] = InnerCaseBody2(p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'InnerCaseBody2')


def p_innercasebody3(p):
    '''innercasebody : WHEN FALSE THEN LPARENT instructions RPARENT innercasebody'''
    p[0] = InnerCaseBody3(p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'InnerCaseBody3')


def p_innercasebodyEmpty(p):
    '''innercasebody : empty'''


def p_condition1(p):
    '''condition : ID comparator ID'''
    p[0] = Condition1(p[1], p[2], p[3], 'Condition1')


def p_condition2(p):
    '''condition : ID comparator NUMBER'''
    p[0] = Condition2(p[1], p[2], p[3], 'Condition2')


def p_condition3(p):
    '''condition : NUMBER comparator ID'''
    p[0] = Condition3(p[1], p[2], p[3], 'Condition3')


def p_condition4(p):
    '''condition : NUMBER comparator NUMBER'''
    p[0] = Condition4(p[1], p[2], p[3], 'Condition4')


def p_condition5(p):
    '''condition : TRUE'''
    p[0] = Condition5(p[1], 'Condition5')


def p_condition6(p):
    '''condition : FALSE'''
    p[0] = Condition6(p[1], 'Condition6')


def p_condition7(p):
    '''condition : istrue'''
    p[0] = Condition7(p[1], 'Condition7')


def p_istrue(p):
    '''istrue : VERT LPARENT ID RPARENT'''
    p[0] = IsTrue(p[1], p[2], p[3], p[4], 'IsTrue')


def p_printstart(p):
    '''printstart : startvalue printvalues'''
    p[0] = PrintStart(p[1], p[2], 'PrintStart')


def p_printvalues1(p):
    '''printvalues : COMMA STRING printvalues'''
    p[0] = PrintValues1(p[1], p[2], p[3], 'PrintValues1')


def p_printvalues2(p):
    '''printvalues : COMMA ID printvalues'''
    p[0] = PrintValues2(p[1], p[2], p[3], 'PrintValues2')


def p_printvaluesEmpty(p):
    '''printvalues : empty'''
    p[0] = NullNode()


def p_startvalue1(p):
    '''startvalue : STRING'''
    p[0] = StartValue1(p[1], 'StartValue1')


def p_startvalue2(p):
    '''startvalue : ID'''
    p[0] = StartValue2(p[1], 'StartValue2')


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    global err
    global errorCounter
    errorCounter = errorCounter + 2
    if p:
        if p.type != 'COMMENT' and p.lineno == 1:
            err = "Syntax error on line 1: Missing expected initial comment."
        else:
            err = "Syntax error on line %d: %s does not match %s position." % (p.lineno, p.value, p.type)


def syntax_analysis(path):
    global errorCounter
    parser = yacc.yacc('LALR')
    result = parser.parse(open(path).read())
    if (errorCounter == 0):
        errorCounter = -1
