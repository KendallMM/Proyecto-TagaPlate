import re

import SyntaxAnalyzer as sx

print_txt = ''


def execute(function):
    if function.name == 'Instructions2':
        return values(function.son3, function.son5.son1)
    elif function.name == 'Instructions3':
        return alter(function.son3, function.son5.son1, function.son7.son1)
    elif function.name == 'Instructions4':
        return alter_b(function.son3)
    elif function.name == 'Instructions5':
        return move_right()
    elif function.name == 'Instructions6':
        return move_left()
    elif function.name == 'Instructions7':
        return hammer(function.son3.son1)
    elif function.name == 'Instructions8':
        return stop()
    elif function.name == 'Instructions12':
        if function.son1.name == 'CaseBody1':
            return case1(function.son1.son4, function.son1.son8)
        elif function.son1.name == 'CaseBody3':
            return case3(function.son1.son2, function.son1.son3.son2, function.son1.son3.son5)
    elif function.name == 'Instructions13':
        return printer(function.son3)
    elif function.name == 'Instructions14':
        return is_true(function.son1.son3)
    else:
        pass


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


def move_right():
    print('Parte de Marco')


def move_left():
    print('Parte de Marco')


def hammer(pos):
    if pos == 'N':
        print('Marco norte')
    elif pos == 'S':
        print('Marco sur')
    elif pos == 'E':
        print('Marco este')
    elif pos == 'O':
        print('Marco oeste')


def stop():
    print('Parte Marco')


def case1(condition, instructions):
    numbers = find_condition(condition)
    count = function_counter(instructions)
    if condition.son2.son1 == '>' and numbers[0] > numbers[1]:
        return recursive_execution(instructions, instructions, count, count)
    elif condition.son2.son1 == '<' and numbers[0] < numbers[1]:
        return execute(instructions)
    elif condition.son2.son1 == '>=' and numbers[0] >= numbers[1]:
        return execute(instructions)
    elif condition.son2.son1 == '<=' and numbers[0] <= numbers[1]:
        return execute(instructions)
    elif condition.son2.son1 == '==' and numbers[0] == numbers[1]:
        return execute(instructions)
    elif condition.son2.son1 == '<>' and numbers[0] != numbers[1]:
        return execute(instructions)


def case3(name, value, instructions):
    print('Hola')


def printer(args):
    global print_txt
    if args.son1[0] == "\"":
        print_txt = args.son1
    else:
        for v in sx.global_vars:
            if v[0] == args.son1:
                print_txt = v[2]


def is_true(name):
    for v in sx.global_vars:
        if v[0] == name:
            if v[2] == 'True':
                return True
            elif v[2] == 'False':
                return False
        else:
            pass


def find_condition(condition):
    num1 = 0
    num2 = 0
    if re.search('\d+', condition.son1):
        num1 = int(condition.son1)
    else:
        for x in sx.global_vars:
            if x[0] == condition.son1:
                num1 = int(x[2])
    if re.search('\d+', condition.son3):
        num2 = int(condition.son3)
    else:
        for y in sx.global_vars:
            if y[0] == condition.son3:
                num2 = int(y[2])
    return num1, num2


def function_counter(function):
    counter = 0
    while function.nexxt.name != 'Null':
        counter += 1
        function = function.nexxt
    return counter


def recursive_execution(first, func, counter, instructions):
    if instructions == 0:
        return execute(func)
    if counter == 0:
        execute(func)
        return recursive_execution(first, first, instructions - 1, instructions - 1)
    else:
        counter -= 1
        func = func.nexxt
        return recursive_execution(first, func, counter, instructions)