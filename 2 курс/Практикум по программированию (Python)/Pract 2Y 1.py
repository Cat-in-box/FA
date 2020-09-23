# -*- coding: utf-8 -*-
from tkinter import *
import math
root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()
 
ball = c.create_oval(100, 100, 500, 500, fill='yellow')
dot = c.create_oval(490, 300, 510, 320, fill='black')

n = 0

def motion():
    global n
    n-=0.1
    x = 20 * math.sin(n)
    y = 20 * math.cos(n)
    c.move(dot, x, y)
    root.after(20, motion)
 
motion()

root.mainloop()