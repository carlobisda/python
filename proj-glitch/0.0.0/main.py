# GLITCH BETA, a personal AI bot written in Python to improve
# productivity. 

from tkinter import * #this will import everything from tkinter
#import backend // will add later when polishing
import os

def add_task():
    print ("test")

window=Tk() #case sensitive, will create empty Win10 window
window.title("gl1tch")

options = Menu(window)
window.config(menu=options)

file = Menu(options)
options.add_cascade(label='File', menu=file)
file.add_command(label='Task', command=add_task)


window.mainloop() 
#always in the end, will ensure window is always open

print("Program Completed!")
