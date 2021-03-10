from tkinter import * #this will import everything from tkinter
import time
import os

window=Tk() #case sensitive, will create empty Win10 window
window.wm_title("gl1tch")

t1=Label(window,text="What can I do for you today master?")
t1.grid(row=0,column=0)

b1=Button(window,text="Add Reminder") 
b1.grid(row=2,column=0)

b2=Button(window,text="View Reminder") 
b2.grid(row=3,column=0)

window.mainloop() 
#always in the end, will ensure window is always open

print("Program Completed!")
