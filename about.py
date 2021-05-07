#!/bin/env python
import tkinter as Tk
from tkinter import *

about = Tk()
about.title("About termux-desktop")
about.geometry("320x200")

text = Label(about, text="""
Termux-desktop-xfce is an active project with
the aim of giving a unique look to termux x11
""")

text.pack()

mensaje = Label(about, text="Tank you for interest in termux-desktop-xfce!", fg="red")
mensaje.pack()

creador = Label(about, text=" - The Yisus Development Team", fg="green")
creador.pack()


about.mainloop()
