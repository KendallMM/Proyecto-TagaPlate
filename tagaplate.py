# IDE CODE TAGAPLATE

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import lexicalAnalyzer as lx
import syntaxAnalyzer as sx

# GLOBAL VARIABLES
gpath = ''
saved = False
err_row = 1

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

#____________________________________ File Functions ___________________________________________________________________

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
        delete()
        file.close()
        gpath = path
        lineText.on_key_release('<Enter>')
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
        delete()
        gpath = path
        file.close()
        lineText.on_key_release('<Enter>')
        highlight_keywords('<Enter>')
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
    else:
        saved = False
        print("No file selected")

#________________________________________ Compile and Run Functions ____________________________________________________

def compile():
    global gpath, saved
    if (gpath == '') or (gpath != '' and not saved):
        compile_aux()
    else:
        lx.lexical_analisis(gpath)
        lexical_error_check()
        sx.sintax_analisis(gpath)
        sintax_error_check()

def compile_aux():
    if ask_to_save() == 'yes':
        save_as()
        compile()
    else:
        w_errors("Can't compile without saving file")
        showErrors()
        tk.messagebox.showinfo('Uncompiled', "Can't compile without saving file", icon='warning')

def ask_to_save():
    return tk.messagebox.askquestion('Save first', 'Do you want to save your file?', icon='warning')

#____________________________________________ Print Management Functions _______________________________________________

def print_path():
    if gpath == '':
        print("Empty")
    else:
        print(gpath)

#__________________________________________ IDE Modifier Functions _____________________________________________________

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
    words = {'Principal': 'yellow',
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
        startIndex = '1.0'
        while True:
            startIndex = textEditor.search(k, startIndex, tk.END)
            if startIndex:
                endIndex = textEditor.index('%s+%dc' % (startIndex, (len(k))))
                textEditor.tag_add(k, startIndex, endIndex)
                textEditor.tag_config(k, foreground=c)
                startIndex = endIndex
            else:
                break

# _________________________________________ Error Management Functions _________________________________________________

def showErrors():
    lx.err = ''
    sx.err = ''
    errorW.deiconify()

def exitErrors():
    errorW.withdraw()

def w_errors(messageError):
    global err_row
    t.config(state='normal')
    t.insert(str(err_row) + '.0', messageError+"\n")
    err_row += 1
    t.pack()
    t.config(state='disabled')

def lexical_error_check():
    if lx.err != '':
        w_errors(lx.err)
        showErrors()
    else:
        pass

def sintax_error_check():
    if sx.err != '':
        w_errors(sx.err)
        showErrors()
    else:
        pass
    if (sx.errorCounter==-1):
        w_errors("El código no presenta errores! :D")

def delete():
    t.config(state='normal')
    t.delete('1.0', tk.END)
    t.config(state='disabled')

errorW = tk.Toplevel(main)
errorW.title("TagaPlate - Errors")
errorW.geometry("500x300")
errorW.protocol("WM_DELETE_WINDOW", exitErrors)
errorW.withdraw()
t = tk.Text(errorW)
t.config(foreground='red', state='disabled')

#________________________________________ IDE Editor ___________________________________________________________________

textEditor = tk.Text()
textEditor.config(background='white', foreground='black')
textEditor.pack(side=tk.RIGHT, expand=1)
textEditor.bind('<Key>', highlight_keywords)

lineText = LineNumber(main, textEditor, width=1)
lineText.pack(side=tk.LEFT)

#___________________________________________ IDE Menu Management _______________________________________________________

menuBar = tk.Menu(main)

fileBar = tk.Menu(menuBar, tearoff=0)
fileBar.add_command(label='New File', command=new_file)
fileBar.add_command(label='Open File', command=open_file)
fileBar.add_command(label='Save File As', command=save_as)
menuBar.add_cascade(label='File', menu=fileBar)

runBar = tk.Menu(menuBar, tearoff=0)
runBar.add_command(label='Compile', command=compile)
runBar.add_command(label='Compile and Run', command=delete)
menuBar.add_cascade(label='Run', menu=runBar)

themeBar = tk.Menu(menuBar, tearoff=0)
themeBar.add_command(label='Dark', command=set_dark)
themeBar.add_command(label='Light', command=set_light)

secondWindows = tk.Menu(menuBar, tearoff=0)
secondWindows.add_command(label='Errors window', command=showErrors)
#secondWindows.add_command(label='Prints window', command=set_light)

menuBar.add_cascade(label='Theme', menu=themeBar)
menuBar.add_cascade(label='Windows', menu=secondWindows)

menuBar.add_command(label='FLUSH', command=delete)
#_______________________________________________________________________________________________________________________

main.config(menu=menuBar)
main.mainloop()
