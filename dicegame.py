import Tkinter
from Tkinter import *
import  random
top=Tkinter.Tk()
text=Tkinter.Text(top,height=2,width=60,foreground="red",font=40)
text.insert(INSERT,"      ROLL THE DICE ! ")
text.pack()
text1=Tkinter.Text(top,height=2,width=60,foreground="blue",font=20)
text2=Tkinter.Text(top,height=2,width=10,foreground="green",font=30)
def call():
  text1.pack_forget()
  text2.pack_forget()
  text1.delete(1.0,END)
  text2.delete(1.0,END) 
  text1.insert(INSERT,"  rolling the dice....the value is...")
  text1.pack()
  
  text2.insert(INSERT,random.randint(1,6))
  text2.pack()

A=Tkinter.Button(top,text="Roll",command=call)
A.pack()

top.mainloop()
