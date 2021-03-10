
from tkinter import * #this will import everything from tkinter

window=Tk() #case sensitive, will create empty Win10 window

def km_to_miles(): #logic behind the gui
    #print(el_value.get))
    miles=float(el_value.get())*1.6 #changed to float
    t1.insert(END,miles) #will insert to text field

b1=Button(window,text="Enter",command=km_to_miles) #first variable set, command is self explanatory
b1.grid(row=1,column=0) 
#sets the b1 button in the window, can also use b1.grid or pack

e1=Entry(window) #entry field
e1.grid(row=1,column=1) #placement control

t1=Text(window,height=1,width=20) #text output
t1.grid(row=1,column=3) #placement control, size control


window.mainloop() 
#always in the end, will ensure window is always open
