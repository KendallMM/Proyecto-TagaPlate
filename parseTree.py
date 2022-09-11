tree_code = ''


class Node:
    pass


class NullNode(Node):
    def __init__(self):
        self.name = 'Null'


class Program(Node):
    def __init__(self, son1, son2, son3, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.name = name

    def create(self):
        global tree_code
        tree_code += '[' + self.name + '\n\t'


class PrincipalProc(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.name = name


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


