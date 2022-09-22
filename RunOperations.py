import SyntaxAnalyzer as sx

print_txt = ''

def execute(function):
    if function.name == 'Instructions2':
        return values(function.son3, function.son5.son1)
    elif function.name == 'Instructions3':
        return alter(function.son3, function.son5.son1, function.son7.son1)
    elif function.name == 'Instructions4':
        return alter_b(function.son3)
    elif function.name == 'Instructions13':
        return printer(function.son3)


def values(name, value):
    for v in sx.global_vars:
        if v[0] == name:
            v[2] = value


def alter(name, op, value):
    for v in sx.global_vars:
        if v[0] == name:
            if op == 'ADD':
                v[2] = str(int(v[2]) + int(value))
                return v
            elif op == 'SUB':
                v[2] = str(int(v[2]) - int(value))
                return v
            elif op == 'MUL':
                v[2] = str(int(v[2]) * int(value))
                return v
            elif op == 'DIV':
                v[2] = str(int(v[2]) / int(value))
                return v


def alter_b(name):
    for v in sx.global_vars:
        if v[0] == name:
            if v[2] == 'True':
                v[2] = 'False'
                return v
            else:
                v[2] = 'True'
                return v


#def hammer(dir):
 #   if dir == 'N':
  #  elif dir == 'S':
   # elif dir == 'E':
    #elif dir == 'O':


def printer(args):
    global print_txt
    if args.son1[0] == "\"":
        print_txt = args.son1
    else:
        for v in sx.global_vars:
            if v[0] == args.son1:
                print_txt = v[2]

