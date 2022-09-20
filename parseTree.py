import re

tree_text = '\n'
init_procs = []
init_vars = []
err = ''


def check_variable(var_name):
    # Check if variable exists
    global err, init_vars
    flag = False
    current = []
    for var in init_vars:
        if var_name == var[0]:
            flag = True
            current.append(var[0])
            current.append(var[1])
            current.append(var[2])
            break
    if not flag:
        err = 'Semantic error: Variable ' + var_name + ' not defined.'
    return current


def check_procedure(proc_name):
    global err, init_procs
    flag = False
    current = ''
    for proc in init_procs:
        if proc_name == proc:
            flag = True
            current = proc_name
            break
    if not flag:
        err = 'Semantic error: ' + proc_name + ' is not a defined procedure.'
    return current


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

        global init_vars
        init_vars.clear()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n'

        text += ident2 + ']'
        return text


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

        global init_vars, init_procs
        init_vars.clear()
        init_procs.append(self.son2)

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
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8 + ']' + '\n' + ident1
        text += '[' + self.son9.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son10.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err, init_vars

        # Valor asignado
        if self.son4.son1 == 'Num' and (self.son6.son1 == 'True' or self.son6.son1 == 'False'):
            err = 'Semantic error: Boolean value cannot be assigned to numeric variable'
        elif self.son4.son1 == 'Bool' and re.search('\d+', self.son6.son1):
            err = 'Semantic error: Number value cannot be assigned to boolean variable'

        # Variable con igual nombre
        for v in init_vars:
            if self.son2 == v[0]:
                err = 'Semantic error: Variable ' + self.son2 + ' defined more than once.'
                break
        init_vars.append([self.son2, self.son4.son1, self.son6.son1])


class Instructions2(Node):
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
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son9.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        # Check if variable type matches with value
        if current[1] == 'Bool' and re.search('\d+', self.son5.son1):
            err = 'Semantic error: Number value cannot be assigned to boolean variable'
        elif current[1] == 'Num' and (self.son5.son1 == 'True' or self.son5.son1 == 'False'):
            err = 'Semantic error: Boolean value cannot be assigned to numeric variable'


class Instructions3(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, son10, son11, name):
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
        self.son11 = son11
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
        text += '[' + self.son10.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son11.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        if current[1] == 'Bool':
            err = 'Semantic error: Cannot operate boolean type variable.'
        elif self.son7.son1 == 'True' or self.son7.son1 == 'False':
            err = 'Semantic error: Cannot operate boolean value.'


class Instructions4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        if current[1] == 'Num':
            err = 'Semantic error: AlterB cannot operate numeric variable.'


class Instructions5(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions6(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions7(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions8(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions9(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions10(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions11(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions12(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions13(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions14(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text


class Instructions15(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.name = name
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son7.printtxt(ident1 + '\t', ident1) + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        check_procedure(self.son3)


class Commentary1(Node):
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
        text += '[' + self.son8 + ']' + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        print(current)
        if current[1] == 'Bool':
            err = 'Semantic error: Cannot operate boolean type variable.'
        elif self.son7.son1 == 'True' or self.son7.son1 == 'False':
            err = 'Semantic error: Cannot operate boolean value.'


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
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current1 = check_variable(self.son1)
        current2 = check_variable(self.son3)
        if current1[1] == 'True' or current1[1] == 'False':
            err = 'Semantic error: Cannot compare boolean variable ' + current1[0] + '.'
        if current2[1] == 'True' or current2[1] == 'False':
            err = 'Semantic error: Cannot compare boolean variable ' + current2[0] + '.'


class Condition2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err, init_vars
        current = check_variable(self.son1)
        print(current)
        if current:
            if current[1] == 'True' or current[1] == 'False':
                err = 'Semantic error: Cannot compare boolean variable ' + current[0] + '.'


class Condition3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        if current[1] == 'True' or current[1] == 'False':
            err = 'Semantic error: Cannot compare boolean variable ' + current[0] + '.'


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
        self.semantics()

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4 + ']' + '\n'

        text += ident2 + ']'
        return text

    def semantics(self):
        global err
        current = check_variable(self.son3)
        if current[1] == 'Num':
            err = 'Semantic error: Variable in IsTrue cannot be numeric.'


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
