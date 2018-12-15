import geek
import luddite
import athelete
import doer
import inspirer
import lazier
import lurker
import nurturer
import ranter
import visionary
import xlsxwriter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import *

f=open('Username.txt','r')
username=f.readline()
f.close()
#loc=location(username)
geek=geek.result
luddite=luddite.result
athelete=athelete.result
doer=doer.result
inspirer=inspirer.result
lazier=lazier.result
lurker=lurker.result
nurturer=nurturer.result
ranter=ranter.result
visionary=visionary.result


def exportdata():
    
    workbook   = xlsxwriter.Workbook("Results/"+username+'.xlsx')
    worksheet1 = workbook.add_worksheet()
    row=0
    col=0
    worksheet1.write(row+0,col,'Personalities')
    worksheet1.write(row+2,col,'Social Athlete')
    worksheet1.write(row+3,col, 'Social Luddite')
    worksheet1.write(row+4,col, 'Social Nurturer')
    worksheet1.write(row+5,col, 'Social Lazies')
    worksheet1.write(row+6,col, 'Social Geek')
    worksheet1.write(row+7,col, 'Social Doer')
    worksheet1.write(row+8,col,'Social Lurker')
    worksheet1.write(row+9,col,'Social Inspirer')
    worksheet1.write(row+10,col,'Social Ranter')
    worksheet1.write(row+11,col,'Social Visionary')

    worksheet1.write(row+0,col+1,'Accuracy')
    worksheet1.write(row+2,col+1,athelete)
    worksheet1.write(row+3,col+1, luddite)
    worksheet1.write(row+4,col+1, nurturer)
    worksheet1.write(row+5,col+1, lazier)
    worksheet1.write(row+6,col+1, geek)
    worksheet1.write(row+7,col+1, doer)
    worksheet1.write(row+8,col+1,lurker)
    worksheet1.write(row+9,col+1,inspirer)
    worksheet1.write(row+10,col+1,ranter)
    worksheet1.write(row+11,col+1,visionary)
    
    #worksheet1.write(row+0,col+2,'Location')
    #worksheet1.write(row+2,col+2,loc)
    workbook.close()


def barchart():
    objects = ('Athlete', 'Luddite', 'Nurturer', 'Lazies', 'Geek', 'Doer','Lurker','Inspirer','Ranter','Visionary')
    y_pos = np.arange(len(objects))
    performance = [athelete,luddite,nurturer,lazier,geek,doer,lurker,inspirer,ranter,visionary]
    width = 0.25
    plt.bar(y_pos, performance, align='center', alpha=0.5,width=width)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.xlabel('Personalities')
    plt.title('Social Media Personality Classification')
    plt.savefig('Results/'+username+'_Barchart'+'.png')
    plt.show()

def piechart():
    labels = 'Athlete', 'Luddite', 'Nurturer', 'Lazies', 'Geek', 'Doer','Lurker','Inspirer','Ranter','Visionary'
    sizes = [athelete,luddite,nurturer,lazier,geek,doer,lurker,inspirer,ranter,visionary]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.savefig('Results/'+username+'_Piechart'+'.png')
    plt.show()




def fun0():
    root = Tk()
    frame = Frame(root)
    frame.pack()
    logo = PhotoImage(file="Image_Content/img_athlete.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    with open('Image_Content/Athelete.txt', 'r') as myfile:
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
    logo = PhotoImage(file="Image_Content/img_lazier.png")
    w1 = Label(frame, image=logo).pack(side=LEFT)
    explanation=[]
    with open('Image_Content/Lazier.txt', 'r') as myfile:
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

def fun8():
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


print(username)
#print(location)
print('geek=',geek)
print('luddite=',luddite)
print('athelete=',athelete)
print('doer=',doer)
print('inspirer=',inspirer)
print('lazier=',lazier)
print('lurker=',lurker)
print('nurturer=',nurturer)
print('ranter=',ranter)
print('visionary=',visionary)
val = [athelete,luddite,nurturer,lazier,geek,doer,lurker,inspirer,ranter,visionary]

#master = Tk()
maxval=val.index(max(val))

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

exportdata()
barchart()
piechart()
