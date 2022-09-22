variables = [['@var1', 'Num', '10'], ['@var2', 'Bool', 'True']]


def alter(name, op, value):
    for v in variables:
        if v[0] == name:
            if op == 'ADD':
                v[2] = str(int(v[2]) + value)
                return v
            elif op == 'SUB':
                v[2] = str(int(v[2]) - value)
                return v
            elif op == 'MUL':
                v[2] = str(int(v[2]) * value)
                return v
            elif op == 'DIV':
                v[2] = str(int(v[2]) / value)
                return v


def alter_b(name):
    for v in variables:
        if v[0] == name:
            if v[2] == 'True':
                v[2] = 'False'
                return v
            else:
                v[2] = 'True'
                return v


print(alter_b('@var2'))
