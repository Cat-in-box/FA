# -*- coding: utf-8 -*-
from tkinter import *
import math
root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()
 
ball = c.create_oval(100, 100, 500, 500, fill='yellow')
dot = c.create_oval(280, 80, 320, 120, fill='black')

n = 0
x = 300
y = 100

def motion():
    global n
    n-=0.1
    x = 200*math.cos(n)
    y = 200*math.sin(n)
    c.move(dot, x, y)
    root.after(10, motion)
 
motion()

root.mainloop()