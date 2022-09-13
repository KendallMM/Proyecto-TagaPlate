printxt = ''


class Node:
    pass


class NullNode(Node):
    def __init__(self):
        self.name = 'Null'

    def printtxt(self):
        return self.name


class Program(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def printtxt(self, ident1):
        global printxt
        printxt += '[' + self.name + '\n' + ident1

        printxt += '[' + self.son1 + ']' + '\n' + ident1
        printxt += '[' + self.son2.printtxt(ident1 + '\t', ident1) + '\n' + ident1
        printxt += '[' + self.son3.printtxt(ident1 + '\t', ident1) + '\n'

        printxt += ']'

        print(printxt)


class Principal(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.name = name

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3.printtxt(ident1 + '\t', ident1) + ']' + '\n' + ident1
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

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + self.son4.printtxt(ident1 + '\t', ident1) + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt() + ']' + '\n'

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

    def printtxt(self, ident1, ident2):
        text = self.name + '\n' + ident1

        text += '[' + self.son1 + ']' + '\n' + ident1
        text += '[' + self.son2 + ']' + '\n' + ident1
        text += '[' + self.son3 + ']' + '\n' + ident1
        text += '[' + 'datatype' + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + 'value' + ']' + '\n' + ident1
        text += '[' + self.son7 + ']' + '\n' + ident1
        text += '[' + self.son8 + ']' + '\n' + ident1
        text += '[' + self.son9.printtxt() + ']' + '\n'

        text += ident2 + ']'
        return text


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
        text += '[' + 'instructions' + ']' + '\n' + ident1
        text += '[' + self.son5 + ']' + '\n' + ident1
        text += '[' + self.son6 + ']' + '\n' + ident1
        text += '[' + self.son7.printtxt() + ']' + '\n'

        text += ident2 + ']'
        return text


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


class Instructions4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name


class Instructions5(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions6(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions7(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name


class Instructions8(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions9(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name


class Instructions10(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions11(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions12(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions13(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name


class Instructions14(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name


class Instructions15(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.name = name


class Instructions16(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


class DataType1(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


class DataType2(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


class Value1(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


class Value2(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


class Value3(Node):
    def __init__(self, son1, name):
        self.son1 = son1
        self.name = name


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


