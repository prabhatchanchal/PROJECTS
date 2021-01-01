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
#function sections
def main_file(a):
    arr=a.split('/')
    return arr[-1]

class work_flow:
    '''This is main class for working with file'''
    def __init__(self):
        self.cur_dir=None
        self.file_name=None
        self.prev=False
    def new_instance(self,file):
        # os.system('python Notepad.py')
        # new_win=Toplevel(root_win)
        os.system(f'python {file}')
        # new_win=Tk()

    def save_as(self,a,root_win):
        try:
            self.file_name=asksaveasfile().name
        except Exception as e:
            return
        file=open(self.file_name,'w')
        file.write(a.get('1.0','end-1c'))
        file.close()
        root_win.title(main_file(self.file_name)+" -- Prabhat's Notepad")
        self.prev=True


    def save(self,a,root_win):
        if not self.prev:
            self.save_as(a,root_win)
        else:
            file=open(self.file_name,'w')
            file.write(a.get('1.0','end-1c'))
            file.close()
            root_win.title(main_file(self.file_name)+" -- Prabhat's Notepad")


    def openn(self,a,root_win):
        try:
            self.file_name=askopenfilename()
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            # print(self.file_name)
            root_win.title(main_file(self.file_name)+" -- Prabhat's Notepad")
            a.insert(END,str(data))
            prev=True
        except Exception as e:
            pass
            
w=work_flow()
#
def bind_save(a,root_win,even):
    w.save(a,root_win)

def new_file_open(a,root):
    w.openn(a,root)

def bind_save_as(a,root_win,event):
    w.save_as(a,root_win)

def bind_new_instance(root_win,event):
    w.new_instance(root_win)

def copy(event):
    # print(event)
    if w.prev:
        cl.copy(a.get('1.0','end-1c'))
def paste(event):
    a.insert(END,str(cl.paste()))
def cut(a):
    # print(event)
    cl.copy(a.get('1.0','end-1c'))
    # print(help(a))
    # a.insert(BEGIN,str(''))
    a.reset()

def dell(a):
    a.delete('1.0','end')

def bind_open(a,root,event):
    w.openn(a,root)
