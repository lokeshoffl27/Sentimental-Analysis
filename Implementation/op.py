from PIL import Image
from tkinter import *


def fun0():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_athlete.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    with open('Image_Content/Athlete.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun1():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_luddite.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Luddite.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun2():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_nurturer.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Nurturer.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun3():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_lazies.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Lazies.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun4():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_geek.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Geek.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun5():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_doer.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Doer.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()


def fun6():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_lurker.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Lurker.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun7():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_inspirer.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Inspirer.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun8():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_ranter.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Ranter.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()

def fun9():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_visionary.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Visionary.txt', 'r') as myfile:
        explanation=" \n".join(line.rstrip() for line in myfile)
    w3 = Label(frame, 
               justify=LEFT,
               padx = 10,
               font = "Helvetica 12 bold",  
               text=explanation).pack(side=RIGHT)

    root.mainloop()



maxval=8

if(maxval==0):
    fun0()
if(maxval==1):
    fun1()
if(maxval==2):
    fun2()
if(maxval==3):
    fun3()
if(maxval==4):
    fun4()
if(maxval==5):
    fun5()
if(maxval==6):
    fun6()
if(maxval==7):
    fun7()
if(maxval==8):
    fun8()
if(maxval==9):
    fun9()
