# IDE CODE TAGAPLATE

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

gpath = ''
saved = False

main = tk.Tk()
main.title("TagaPlate IDE")


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

def new_file():
    global gpath, saved
    path = asksaveasfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    saved = True
    update_title()
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
        file.close()
        gpath = path


def open_file():
    global gpath, saved
    path = askopenfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    saved = True
    update_title()
    if path != '':
        file = open(path, 'r')
        code = file.read()
        textEditor.delete('1.0', tk.END)
        textEditor.insert('1.0', code)
        gpath = path
        file.close()
    else:
        print("No file selected")


def save_as():
    global gpath, saved
    if gpath == '':
        path = asksaveasfilename(filetypes=[('TagaPlate Files', '*.tgp')])
    else:
        path = gpath
    saved = True
    update_title()
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
    else:
        print("No file selected")

def compile():
    global gpath
    if gpath == '':
        msgbox = tk.messagebox.askquestion('Save first', 'Do you want to save your file?', icon='warning')
        if msgbox == 'yes':
            path = asksaveasfilename(filetypes=[('TagaPlate File', '*.tgp')])
            gpath = path
            if path != '':
                file = open(path, 'w')
                file.write(textEditor.get('1.0', tk.END))
                file.close()
                compile()
        else:
            w_errors("Can't compile without saving file")
    elif gpath != '':
        print("Compile process")

def set_dark():
    textEditor.config(background='black', foreground='white')

def set_light():
    textEditor.config(background='white', foreground='black')

def print_path():
    if gpath == '':
        print("Empty")
    else:
        print(gpath)

def update_title():
    global saved
    if saved:
        main.title('TagaPlate IDE')
    else:
        main.title('TagaPlate IDE *')

def w_errors(message):
    minwin = tk.Toplevel()
    label = tk.Label(minwin, text=message, background='white', foreground='red')
    label.place(x=0, y=0)

def highlight_keywords(event):
    words = {'New': 'blue',
             'True': 'blue',
             'False': 'blue',
             'While': 'blue',
             'Until': 'blue',
             'Case': 'blue',
             'When': 'blue',
             'Then': 'blue',
             'Else': 'blue',
             'Break': 'blue',
             'Values': 'red',
             'Alter': 'red',
             'AlterB': 'red',
             'MoveRight': 'red',
             'MoveLeft': 'red',
             'Hammer': 'red',
             'Stop': 'red',
             'isTrue': 'red',
             'Repeat': 'red',
             'PrintValues': 'red'}
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

textEditor = tk.Text()
textEditor.config(background='white', foreground='black')
textEditor.pack(side=tk.RIGHT, expand=1)
textEditor.bind('<Key>', highlight_keywords)

lineText = LineNumber(main, textEditor, width=1)
lineText.pack(side=tk.LEFT)

menuBar = tk.Menu(main)

fileBar = tk.Menu(menuBar, tearoff=0)
fileBar.add_command(label='New File', command=new_file)
fileBar.add_command(label='Open File', command=open_file)
fileBar.add_command(label='Save File As', command=save_as)
menuBar.add_cascade(label='File', menu=fileBar)

runBar = tk.Menu(menuBar, tearoff=0)
runBar.add_command(label='Compile', command=compile)
runBar.add_command(label='Compile and Run')
menuBar.add_cascade(label='Run', menu=runBar)

themeBar = tk.Menu(menuBar, tearoff=0)
themeBar.add_command(label='Dark', command=set_dark)
themeBar.add_command(label='Light', command=set_light)
menuBar.add_cascade(label='Theme', menu=themeBar)

menuBar.add_command(label="PATH", command=print_path)

main.config(menu=menuBar)
main.mainloop()
