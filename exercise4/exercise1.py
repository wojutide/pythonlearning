#!/usr/bin/python3.5

import tkinter as tk

from tkinter import messagebox

top=tk.Tk()
top.geometry("500x500")

def helloCallBack():
    msg=messagebox.showinfo('Hello Python', "Hello World")

B=tk.Button(top, text='Hello',command=helloCallBack)
B.place(x=50,y=50)
top.mainloop()
