# IDE CODE TAGAPLATE

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

gpath = ''

main = tk.Tk()
main.title("TagaPlate IDE")
err_frame = tk.Toplevel(main)
prt_frame = tk.Toplevel(main)

class LineNumber(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_release(self, event=None):
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

def open_file():
    global gpath
    path = askopenfilename(filetypes=[('Text Files', '*.txt')])
    if path != '':
        with open(path, 'r') as file:
            code = file.read()
            textEditor.delete('1.0', tk.END)
            textEditor.insert('1.0', code)
            gpath = path
    else:
        print("No file selected")


def save_as():
    global gpath
    if gpath == '':
        path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])
    else:
        path = gpath
    if path != '':
        with open(path, 'w') as file:
            code = textEditor.get('1.0', tk.END)
            file.write(code)
    else:
        print("No file selected")

#def close_window(option):


#def open_errframe():


#def open_prframe():


textEditor = tk.Text()
textEditor.pack(side=tk.RIGHT, expand=1)

lineText = LineNumber(main, textEditor, width=1)
lineText.pack(side=tk.LEFT)

lineText1 = LineNumber(err_frame, textEditor, width=1)
lineText1.pack(side=tk.LEFT)

lineText2 = LineNumber(prt_frame, textEditor, width=1)
lineText2.pack(side=tk.LEFT)

menuBar = tk.Menu(main)

fileBar = tk.Menu(menuBar, tearoff=0)
fileBar.add_command(label='Edit file', command=open_file)
fileBar.add_command(label='Save file as', command=save_as)
menuBar.add_cascade(label='File', menu=fileBar)

menuBar.add_command(label='Compile')
menuBar.add_command(label='Compile and Run')

seeBar = tk.Menu(menuBar, tearoff=0)
#seeBar.add_command(label='Errors', command=open_errframe)
#seeBar.add_command(label='Prints', command=open_prframe)
menuBar.add_cascade(label='See', menu=seeBar)

main.config(menu=menuBar)

#ERR_WINDOW.protocol("WM_DELETE_WINDOW", close_window(1))
#PRI_WINDOW.protocol("WM_DELETE_WINDOW", close_window(2))
main.mainloop()
