class Node:
    pass


class NullNode(Node):
    def __init__(self):
        self.value = 'Nulo'


class Program(Node):
    def __init__(self, value, son1, son2):
        self.value = value
        self.son1 = son1
        self.son2 = son2


class BodyProgram(Node):
    def __init__(self, value, son1, son2):
        self.value = value
        self.son1 = son1
        self.son2 = son2
