import Tkinter
from Tkinter import *
import tkMessageBox
top=Tkinter.Tk()
text=Tkinter.Text(top,height=2,width=60,foreground="red",font=40)
text.insert(INSERT,"      CHOOSE YOUR LUCKY NUMBER !  ")
text.pack()
def call1():
   tkMessageBox.showinfo("1","One moment at a time.If we live that way,\nwithout worrying about tomorrow and regretting\nabout yesterday, life would be much\neasier to deal with.Take it easy!\nYesterday is long gone and tomorrow\nwe may never see.What we have is this\nvery moment.Seize it!")
def call2():
   tkMessageBox.showinfo("2","No matter what life brings\nto you, no matter how the world\ntreats you, how you respond\nto them is in your hands.\nIf you respond being a\nvictim, then you are being mechanical.\nTake charge of your of life!")
def call3():
   tkMessageBox.showinfo("3","Every challenge , every failure is\nis yet another opportunity to transcend \nour weaknesses, an opportunity for\nus to grow.It is alright if you\nslip.But bounce back!\nKeep going. one step at a time!")
def call4():
   tkMessageBox.showinfo("4","Let your smile change the world.\nDon't let the world change\nyour smile.Find a reason to smile.\nThere are many more reasons to\nsmile than not smile.\nFind those reasons!")
def call5():
   tkMessageBox.showinfo("5","Are you doing all that is needed\nto unleash your potential\nand develope it to the heights of perfection?\nOr are you just sitting around for\nmiracles to happen ?\nMiracles work when we work!") 
def call6():
   tkMessageBox.showinfo("6","Our real strength is in the\nbest we can be.Find out what it is that makes\nyou tick;what it is that drives you;what it\nis that you are ready to do for the rest\nof your life no matter what.Once you\nfind that, go all out to be the best in that.\nPractice does make perfect!")
A=Tkinter.Button(top,text="1",command=call1)
B=Tkinter.Button(top,text="2",command=call2)
C=Tkinter.Button(top,text="3",command=call3)
D=Tkinter.Button(top,text="4",command=call4)
E=Tkinter.Button(top,text="5",command=call5)
F=Tkinter.Button(top,text="6",command=call6)
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
top.mainloop()
