# IDE CODE TAGAPLATE

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import LexicalAnalyzer as lx
import SyntaxAnalyzer as sx
import ParseTree as prs
from pymata4 import pymata4
import time

# GLOBAL VARIABLES
gpath = ''
saved = False
err_row = 1
pr_row = 1

runnable = False
compilation_errors = 0
print_txt = ''

board = pymata4.Pymata4()
angle = 90
anglesPerSecond = 9
board.set_pin_mode_servo(5)
board.set_pin_mode_servo(7)
num_steps_clockwise = 512
num_steps_counterclockwise = -512
pins = [8,10,9,11]
board.set_pin_mode_stepper(num_steps_clockwise, pins)

# MAIN WINDOW
main = tk.Tk()
main.title("TagaPlate IDE")


# _________________________________________ Line Number Class __________________________________________________________

class LineNumber(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_release(self, event=None):
        global saved, lineno
        p, q = self.text_widget.index("@0,0").split('.')
        p = int(p)
        final_index = str(self.text_widget.index(tk.END))
        num_of_lines = final_index.split('.')[0]
        lines = '\n'.join(str(p + no) for no in range(int(num_of_lines) - 1))
        width = len(str(num_of_lines))
        self.configure(state='normal', width=width)
        self.delete(1.0, tk.END)
        self.insert(1.0, lines)
        self.configure(state='disabled')
        saved = False
        update_title()


# ____________________________________ File Functions ___________________________________________________________________

def new_file():
    global gpath, saved
    path = asksaveasfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    if path != '':
        if not path.endswith(".tgp"):
            path += ".tgp"
        else:
            pass
        file = open(path, 'w')
        welcome = 'Welcome to new TagaPlate File!'
        file.write(welcome)
        textEditor.delete('1.0', tk.END)
        textEditor.insert('1.0', welcome)
        delete_errors()
        delete_prints()
        file.close()
        gpath = path
        lineText.on_key_release('<Enter>')
        reset_file()
    saved = True
    update_title()


def open_file():
    global gpath, saved
    path = askopenfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    if path != '':
        file = open(path, 'r')
        code = file.read()
        textEditor.delete('1.0', tk.END)
        textEditor.insert('1.0', code)
        delete_errors()
        delete_prints()
        gpath = path
        file.close()
        lineText.on_key_release('<Enter>')
        highlight_keywords('<Enter>')
        reset_file()
    else:
        print("No file selected")
    saved = True
    update_title()


def save_as():
    global gpath, saved
    if gpath == '':
        path = asksaveasfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    else:
        path = gpath
    if path != '':
        if not path.endswith(".tgp"):
            path += ".tgp"
        else:
            pass
        file = open(path, 'w')
        code = textEditor.get('1.0', tk.END)
        file.write(code)
        file.close()
        gpath = path
        saved = True
        update_title()
        reset_file()
    else:
        saved = False
        print("No file selected")


def reset_file():
    lx.err = ''
    sx.err = ''
    prs.err = ''
    prs.global_vars.clear()
    prs.local_vars.clear()
    prs.init_procs.clear()
    prs.called_procs.clear()


# ________________________________________ Compile and Run Functions ____________________________________________________


def compile():
    global gpath, saved, compilation_errors, runnable
    if (gpath == '') or (gpath != '' and not saved):
        compile_aux()
    else:
        compilation_errors = 0
        runnable = False
        prs.global_vars.clear()
        prs.init_procs.clear()
        lx.lexical_analisis(gpath)
        lexical_error_check()
        sx.syntax_analysis(gpath)
        syntax_error_check()
        semantic_error_check()
        print('Errors during compilation: ' + str(compilation_errors))
        if compilation_errors == 0:
            runnable = True


def compile_aux():
    if ask_to_save() == 'yes':
        save_as()
        compile()
    else:
        w_errors("Can't compile without saving file")
        show_errors()
        tk.messagebox.showinfo('Uncompiled', "Can't compile without saving file", icon='warning')


def run():
    global runnable, print_txt
    compile()
    runnable_tree = sx.sem_tree.son3.son3
    print_txt = ''
    delete_prints()
    if runnable and runnable_tree:
        counter = function_counter(runnable_tree)
        return recursive_execution(runnable_tree, runnable_tree, counter, counter)


def function_counter(function):
    counter = 0
    while function.nexxt.name != 'Null':
        counter += 1
        function = function.nexxt
    return counter


def recursive_execution(first, func, counter, instructions):
    if instructions == 0:
        execute(func)
        write_printer()
        return
    if counter == 0:
        execute(func)
        write_printer()
        return recursive_execution(first, first, instructions - 1, instructions - 1)
    else:
        counter -= 1
        func = func.nexxt
        return recursive_execution(first, func, counter, instructions)


def execute(function):
    if function.name == 'Instructions2':
        return values(function.son3, function.son5.son1)
    elif function.name == 'Instructions3':
        return alter(function.son3, function.son5.son1, function.son7.son1)
    elif function.name == 'Instructions4':
        return alter_b(function.son3)
    elif function.name == 'Instructions5':
        time.sleep(1)
        return move_right()
    elif function.name == 'Instructions6':
        time.sleep(1)
        return move_left()
    elif function.name == 'Instructions7':
        return hammer(function.son3.son1)
    elif function.name == 'Instructions8':
        return stop()
    elif function.name == 'Instructions10':
        return until_function(function.son1.son5, function.son1.son3)
    elif function.name == 'Instructions12':
        if function.son1.name == 'CaseBody1':
            return case1(function.son1.son4, function.son1.son8, function.son1.son10)
    elif function.name == 'Instructions13':
        return printer(function.son3)
    elif function.name == 'Instructions14':
        return is_true(function.son1.son3)
    elif function.name == 'Instructions15':
        return call_function(function.son3, sx.sem_tree.son2, sx.sem_tree.son4)
    elif function.name == 'Instructions11':
        While(function.son1.son2, function.son1.son4)
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
    global num_steps_clockwise
    board.stepper_write(63, num_steps_clockwise)
    time.sleep(1)
    board.stepper_write(63, num_steps_clockwise)
    time.sleep(1)


def move_left():
    global num_steps_counterclockwise
    board.stepper_write(63, num_steps_counterclockwise)
    time.sleep(1)
    board.stepper_write(63, num_steps_counterclockwise)
    time.sleep(1)

def rotateServo(pin, angle):
    board.servo_write(pin, angle)
    time.sleep(0.015)

def hammer(pos):
    if pos == 'N':
        global angle
        if angle + anglesPerSecond < 180:
            for i in range(0, 5):
                angle = angle + anglesPerSecond
                rotateServo(7, angle)
            for i in range(0, 5):
                angle = angle - anglesPerSecond
                rotateServo(7, angle)
    elif pos == 'S':
        global angle
        if angle - anglesPerSecond > 0:
            for i in range(0, 5):
                angle = angle - anglesPerSecond
                rotateServo(7, angle)
            for i in range(0, 5):
                angle = angle + anglesPerSecond
                rotateServo(7, angle)
    elif pos == 'E':
        global angle
        if angle + anglesPerSecond < 180:
            for i in range(0, 5):
                angle = angle + anglesPerSecond
                rotateServo(5, angle)
            for i in range(0, 5):
                angle = angle - anglesPerSecond
                rotateServo(5, angle)
    elif pos == 'O':
        global angle
        if angle - anglesPerSecond > 0:
            for i in range(0, 5):
                angle = angle - anglesPerSecond
                rotateServo(5, angle)
            for i in range(0, 5):
                angle = angle + anglesPerSecond
                rotateServo(5, angle)


def stop():
    print('Parte Marco')


def until_function(condition, instructions):
    numbers = find_condition(condition)
    count = function_counter(instructions)
    if condition.son2.son1 == '==' and numbers[0] != numbers[1]:
        while numbers[0] != numbers[1]:
            recursive_execution(instructions, instructions, count, count)
            numbers = find_condition(condition)
    elif (condition.son2.son1 == '>' or condition.son2.son1 == '>=') and numbers[0] < numbers[1]:
        while numbers[0] < numbers[1]:
            recursive_execution(instructions, instructions, count, count)
            numbers = find_condition(condition)
    elif (condition.son2.son1 == '<' or condition.son2.son1 == '<=') and numbers[0] > numbers[1]:
        while numbers[0] > numbers[1]:
            recursive_execution(instructions, instructions, count, count)
            numbers = find_condition(condition)
    elif condition.son2.son1 == '<>' and numbers[0] == numbers[1]:
        while numbers[0] == numbers[1]:
            recursive_execution(instructions, instructions, count, count)
            numbers = find_condition(condition)


def case1(condition, instructions, next_case):
    count = function_counter(instructions)
    if condition.name == 'Condition7':
        if is_true(condition.son1.son3):
            return recursive_execution(instructions, instructions, count, count)
        elif next_case.name != 'NullNode':
            if next_case.name == 'CaseBody1':
                return case1(next_case.son4, next_case.son8, next_case.son10)
            elif next_case.name == 'CaseBody2' and next_case.son1.name == 'CaseElse1' and next_case.son1.name != 'NullNode':
                return recursive_execution(next_case.son1.son3, next_case.son1.son3, count, count)
    elif condition.name != 'Condition7':
        numbers = find_condition(condition)
        if condition.son2.son1 == '>' and numbers[0] > numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif condition.son2.son1 == '<' and numbers[0] < numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif condition.son2.son1 == '>=' and numbers[0] >= numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif condition.son2.son1 == '<=' and numbers[0] <= numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif condition.son2.son1 == '==' and numbers[0] == numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif condition.son2.son1 == '<>' and numbers[0] != numbers[1]:
            return recursive_execution(instructions, instructions, count, count)
        elif next_case.name != 'Null':
            if next_case.name == 'CaseBody1':
                return case1(next_case.son4, next_case.son8, next_case.son10)
            elif next_case.name == 'CaseBody2' and next_case.son1.name == 'CaseElse1' and next_case.son1.name != 'NullNode':
                return recursive_execution(next_case.son1.son3, next_case.son1.son3, count, count)


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


def call_function(proc_name, left, right):
    if left.name != 'Null' and right.name != 'Null':
        if proc_name == left.son2:
            return recursive_execution(left.son4, left.son4, function_counter(left.son4), function_counter(left.son4))
        if proc_name == right.son2:
            return recursive_execution(right.son4, right.son4, function_counter(right.son4), function_counter(right.son4))
        else:
            return call_function(proc_name, left.nexxt, right.nexxt)
    elif left.name == 'Null' and right.name != 'Null':
        if proc_name == right.son2:
            return recursive_execution(right.son4, right.son4, function_counter(right.son4), function_counter(right.son4))
        else:
            return call_function(proc_name, left, right.nexxt)
    elif left.name != 'Null' and right.name == 'Null':
        if proc_name == left.son2:
            return recursive_execution(left.son4, left.son4, function_counter(left.son4), function_counter(left.son4))
        else:
            return call_function(proc_name, left.nexxt, right)


def find_condition(condition):
    num1 = 0
    num2 = 0
    try:
        num1 = int(condition.son1)
    except:
        for x in sx.global_vars:
            if x[0] == condition.son1:
                num1 = int(x[2])
    try:
        num2 = int(condition.son3)
    except:
        for y in sx.global_vars:
            if y[0] == condition.son3:
                num2 = int(y[2])
    return num1, num2


def While(condition, instructions):
    count = function_counter(instructions)
    if (condition.name == "Condition7"):
        while is_true(condition.son1.son3):
            recursive_execution(instructions, instructions, count, count)
    else:
        values = find_condition(condition)
        if condition.son2.son1 == '>':
            while values[0] > values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)
        if condition.son2.son1 == '<':
            while values[0] < values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)
        if condition.son2.son1 == '>=':
            while values[0] >= values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)
        if condition.son2.son1 == '<=':
            while values[0] <= values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)
        if condition.son2.son1 == '==':
            while values[0] == values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)
        if condition.son2.son1 == '<>':
            while values[0] != values[1]:
                recursive_execution(instructions, instructions, count, count)
                values = find_condition(condition)

def ask_to_save():
    return tk.messagebox.askquestion('Save first', 'Do you want to save your file?', icon='warning')


# __________________________________________ IDE Modifier Functions _____________________________________________________

def set_dark():
    textEditor.config(background='black', foreground='white')


def set_light():
    textEditor.config(background='white', foreground='black')


def update_title():
    global saved
    if saved:
        main.title('TagaPlate IDE')
    else:
        main.title('TagaPlate IDE (not saved)')


def highlight_keywords(event):
    words = {'@Principal': 'orange',
             'New': 'blue',
             'True': 'blue',
             'False': 'blue',
             'While': 'blue',
             'Until': 'blue',
             'Case': 'blue',
             'When': 'blue',
             'Then': 'blue',
             'Else': 'blue',
             'Break': 'blue',
             'Proc': 'blue',
             'Values': 'red',
             'Alter': 'red',
             'AlterB': 'red',
             'MoveRight': 'red',
             'MoveLeft': 'red',
             'Hammer': 'red',
             'Stop': 'red',
             'isTrue': 'red',
             'Repeat': 'red',
             'PrintValues': 'red',
             'CALL': 'red'}
    for k, c in words.items():
        start_index = '1.0'
        while True:
            start_index = textEditor.search(k, start_index, tk.END)
            if start_index:
                end_index = textEditor.index('%s+%dc' % (start_index, (len(k))))
                textEditor.tag_add(k, start_index, end_index)
                textEditor.tag_config(k, foreground=c)
                start_index = end_index
            else:
                break


# _________________________________________ Error Management Functions _________________________________________________

def show_errors():
    lx.err = ''
    sx.err = ''
    errorW.deiconify()


def exit_errors():
    errorW.withdraw()


def w_errors(err_msg):
    global err_row
    t.config(state='normal')
    t.insert(str(err_row) + '.0', err_msg + "\n")
    err_row += 1
    t.pack()
    t.config(state='disabled')


def lexical_error_check():
    global compilation_errors
    if lx.err != '':
        compilation_errors += 1
        w_errors(lx.err)
        show_errors()
    else:
        pass


def syntax_error_check():
    global compilation_errors
    if sx.err != '':
        compilation_errors += 1
        w_errors(sx.err)
        show_errors()
    else:
        pass


def semantic_error_check():
    global compilation_errors
    if prs.err != '':
        compilation_errors += 1
        w_errors(prs.err)
        show_errors()
    else:
        pass


def delete_errors():
    t.config(state='normal')
    t.delete('1.0', tk.END)
    t.config(state='disabled')


errorW = tk.Toplevel(main)
errorW.title("TagaPlate - Errors")
errorW.geometry("500x300")
errorW.protocol("WM_DELETE_WINDOW", exit_errors)
errorW.withdraw()
t = tk.Text(errorW)
t.config(foreground='red', state='disabled')

#_________________________________________ Print Management Functions ___________________________________________________

def show_prints():
    printsW.deiconify()


def exit_prints():
    printsW.withdraw()


def write_printer():
    global print_txt
    if print_txt != '':
        set_print_text(print_txt)
        show_prints()
        print_txt = ''
    else:
        pass


def set_print_text(string):
    global pr_row
    t2.config(state='normal')
    t2.insert(str(pr_row) + '.0', string + '\n')
    pr_row += 1
    t2.pack()
    t2.config(state='disabled')


def delete_prints():
    t2.config(state='normal')
    t2.delete('1.0', tk.END)
    t2.config(state='disabled')


printsW = tk.Toplevel(main)
printsW.title("TagaPlate - Prints")
printsW.geometry("500x300")
printsW.protocol("WM_DELETE_WINDOW", exit_prints)
printsW.withdraw()
t2 = tk.Text(printsW)
t2.config(foreground='green', state='disabled')


# ________________________________________ IDE Editor ___________________________________________________________________

textEditor = tk.Text()
textEditor.config(background='white', foreground='black')
textEditor.pack(side=tk.RIGHT, expand=1)
textEditor.bind('<Key>', highlight_keywords)

lineText = LineNumber(main, textEditor, width=1)
lineText.pack(side=tk.LEFT)


# ___________________________________________ IDE Menu Management _______________________________________________________

menuBar = tk.Menu(main)

fileBar = tk.Menu(menuBar, tearoff=0)
fileBar.add_command(label='New File', command=new_file)
fileBar.add_command(label='Open File', command=open_file)
fileBar.add_command(label='Save File As', command=save_as)
menuBar.add_cascade(label='File', menu=fileBar)

runBar = tk.Menu(menuBar, tearoff=0)
runBar.add_command(label='Compile', command=compile)
runBar.add_command(label='Compile and Run', command=run)
menuBar.add_cascade(label='Run', menu=runBar)

themeBar = tk.Menu(menuBar, tearoff=0)
themeBar.add_command(label='Dark', command=set_dark)
themeBar.add_command(label='Light', command=set_light)

menuBar.add_command(label='Errors', command=show_errors)
menuBar.add_command(label='Prints', command=show_prints)

menuBar.add_cascade(label='Theme', menu=themeBar)
# _______________________________________________________________________________________________________________________

main.config(menu=menuBar)
main.mainloop()
