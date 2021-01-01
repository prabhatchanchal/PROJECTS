from __future__ import unicode_literals
import sys
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.constants import  *
from tkinter import *
from tkinter.filedialog import askdirectory,asksaveasfile,askopenfilename
from functools import  partial
import os
import clipboard as cl
from Notepad_support_file import *
file_=__file__
# Main App sections

app = Tk()

icon = PhotoImage(file='open-book.png')
app.iconphoto(True,icon)
app.minsize(512,480)
app.title('Untitled -- Prabhat\'s Notepad')
text_filed=Text(app,border=9,relief=FLAT,spacing2=1)
text_filed.bind('<Control-s>',partial(bind_save,text_filed,app))
text_filed.bind('<Control-Shift-S>',partial(bind_save_as,text_filed,app))
text_filed.bind('<Control-Shift-N>',partial(bind_new_instance,file_))
text_filed.bind('<Control-c>',copy)
text_filed.bind('<Control-o>',partial(bind_open,text_filed,app))

text_filed.configure(font=('Consolas',11,'roman'))
text_filed.pack(fill=BOTH,expand=1)
menubar=Menu(app)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label='New',command=partial(new_file_open,text_filed,app),accelerator='Ctrl+N')
file.add_command(label='New Window',command=partial(w.new_instance,file_),accelerator='Ctrl+Shift+N')
file.add_command(label='Open..',command=partial(w.openn,text_filed,app),accelerator='Ctrl+O')

file.add_command(label='Save ',command=partial(w.save,text_filed),accelerator='Ctrl+S')
file.add_command(label='Save as',command=partial(w.save_as,text_filed),accelerator='Ctrl+Shift+S')
file.add_separator()
file.add_command(label='Page Setup',command=None)
file.add_command(label='print..',command=None,accelerator='Ctrl+P')
file.add_separator()
file.add_command(label='Exit',command=app.destroy)
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Undo',command=None)
edit.add_separator()
edit.add_command(label='Cut',command=partial(cut,text_filed),accelerator='Ctrl+X')
edit.add_command(label='Copy',command=copy,accelerator='Ctrl+C')
edit.add_command(label='Pase',command=paste,accelerator='Ctrl+V')
edit.add_command(label='Delete',command=partial(dell,text_filed),accelerator='Del')
format=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Format',menu=format)
format.add_command(label='Word Wrap',command=None)
format.add_command(label='Font..',command=None)
Help=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=Help)
Help.add_command(label='View Help',command=None)
Help.add_command(label='Send Feedback',command=None)
Help.add_separator()
Help.add_command(label='About Me',command=None)
Help.add_radiobutton(label='Radio button',command=None)
app.config(menu=menubar)
app.mainloop()
