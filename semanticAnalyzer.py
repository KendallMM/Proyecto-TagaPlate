txt = ""
id = 0

def update_id():
    global id
    id += 1
    return "%d" %id

class Node:
    pass

class Null(Node):
    def __init__(self):
        self.type = 'void'

    def print_op(self, ident):
        print(ident + "Node: Nulo")

    def translate(self):
        global txt
        id = update_id()
        txt += id + "[label= Nulo]\n\t"

        return id

class Program(Node):
    def __init__(self, son2, name):
        self.name = name
        self.son2 = son2

    def print_op(self, ident):
        self.son2.print_op(ident)
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return "digraph G {\n\t" + txt + "}"

class BodyProgram1(Node):
    def __init__(self, son1, son2, name):
        self.son1 = son1
        self.son2 = son2
        self.name = name

    def print_op(self, ident):
        self.son1.print_op(ident)
        self.son2.print_op(ident)
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"
        txt += id + "->" + son2 + "\n\t"

        return id

class BodyProgram2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def print_op(self, ident):
        self.son1.print_op(ident)
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        son1 = self.son1.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son1 + "\n\t"

        return id

class BodyProgram3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self, ident):
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        return id

class BodyProgramEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self, ident):
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        return id

class Procedure1(Node):
    def __init__(self, son3, name):
        self.name = name
        self.son3 = son3

    def print_op(self, ident):
        self.son3.print_op(ident)
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        return id

class Procedure2(Node):
    def __init__(self, son3, name):
        self.name = name
        self.son3 = son3

    def print_op(self, ident):
        self.son3.print_op(ident)
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        son3 = self.son3.translate()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + "->" + son3 + "\n\t"
        return id

class Instructions1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions5(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions6(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions7(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions8(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions9(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions10(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions11(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions12(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions13(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions14(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions15(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Instructions16(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class InstructionsEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class AlterBody(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class DataType1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class DataType2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Value1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Value2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Value3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Value4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Operator1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Operator2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Operator3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Operator4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator5(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Comparator6(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Position1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Position2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Position3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Position4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class RepeatInstructions(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class UntilBody(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class WhileBody(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class CaseBody1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class CaseBody2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class CaseBody3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class InnerCaseBody1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class InnerCaseBody2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class InnerCaseBody3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class InnerCaseBodyEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition3(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition4(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition5(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition6(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition7(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class IsTrue(Node):
    def  __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class PrintValues1(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class PrintValues2(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class PrintValuesEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

##class Empty(Node):
