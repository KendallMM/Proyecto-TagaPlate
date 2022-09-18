import re

tree_text = '\n'
initialized_variables = []
err = ''


class Node:
    pass


class NullNode(Node):
    def __init__(self):
        self.name = 'Null'

    def printtxt(self, ident1, ident2):
        return self.name + ']'


class Program(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1):
        global tree_text
        tree_text += '[' + self.name + '\n' + ident1

        tree_text += '[' + self.son1 + ']' + '\n' + ident1
        tree_text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        tree_text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        tree_text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        tree_text += ']'

        print(tree_text)


class Principal(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.name = name
        self.initialized_variables = []

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n'

        text += ident2 + ']'
        return text

    def initialize(self, name, typo, value):
        self.initialized_variables.append([name, typo, value])


class Procedures(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name
        self.initialized_variables = []

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.name = name
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8 + ']' + '\n' + ident1
        text += '[' + self.son9.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        #Valor asignado
        print(self.son4.son1)
        print(self.son6.son1)
        if self.son4.son1 == 'Num' and (self.son6.son1 == 'True' or self.son6.son1 == 'False'):
            err = 'Semantic error: Boolean value cannot be assigned to numeric variable'
        elif self.son4.son1 == 'Bool' and re.search('\d+', self.son6.son1):
            err = 'Semantic error: Number value cannot be assigned to boolean variable'


class Instructions2(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err



class Instructions3(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, son10, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10
        self.name = name
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son8 + ']' + '\n' + ident1
        text += '[' + self.son9 + ']' + '\n' + ident1
        text += '[' + self.son10.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    #def semantics(self):
     #   global err
      #  if self.son7.son1 == 'True' or self.son7.son1 == 'False':
       #     err = 'Semantic error: Cannot operate boolean value in Alter function.'


class Instructions4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        if re.search('\d+', self.son3.son1):
            err = 'Semantic error: Cannot operate numeric value in AlterB function.'


class Instructions5(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions6(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions7(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions8(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions9(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions10(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions11(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions12(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions13(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions14(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions15(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions16(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class DataType1(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class DataType2(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Value1(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Value2(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Value3(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Value4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son8 + ']' + '\n'

        text += ident2 + ']'
        return text


class Operator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Operator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Operator3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Operator4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Comparator6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Position1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Position2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Position3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Position4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class RepeatInstructions(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n'

        text += ident2 + ']'
        return text


class UntilBody(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class WhileBody(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n'

        text += ident2 + ']'
        return text


class CaseBody1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son9 + ']' + '\n'

        text += ident2 + ']'
        return text


class CaseBody2(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n'

        text += ident2 + ']'
        return text


class CaseBody3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class InnerCaseBody1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class InnerCaseBody2(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class InnerCaseBody3(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Condition1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition4(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class Condition7(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class IsTrue(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n'

        text += ident2 + ']'
        return text


class PrintStart(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class PrintValues1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + ']' + '\n'

        text += ident2 + ']'
        return text


class PrintValues2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class StartValue1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text


class StartValue2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n'

        text += ident2 + ']'
        return text
