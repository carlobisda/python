#BASIC ROULETTE TRACKER v1.0.5
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import sqlite3

#CREATES THE WIN10 GUI
root = Tk()
root.wm_title("Database Analysis")

#CONTROLLING THE DATABASE
def cmnd_1():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (1)")
    conn.commit()
    conn.close()
    
def cmnd_2():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (2)")
    conn.commit()
    conn.close()

def cmnd_3():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (3)")
    conn.commit()
    conn.close()

def cmnd_4():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (4)")
    conn.commit()
    conn.close()

def cmnd_5():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (5)")
    conn.commit()
    conn.close()

def cmnd_6():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk)VALUES (6)")
    conn.commit()
    conn.close()

def cmnd_7():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (7)")
    conn.commit()
    conn.close()

def cmnd_8():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (8)")
    conn.commit()
    conn.close()

def cmnd_9():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (9)")
    conn.commit()
    conn.close()

def cmnd_10():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (10)")
    conn.commit()
    conn.close()

def cmnd_11():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (11)")
    conn.commit()
    conn.close()

def cmnd_12():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (12)")
    conn.commit()
    conn.close()

def cmnd_13():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (13)")
    conn.commit()
    conn.close()

def cmnd_14():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (14)")
    conn.commit()
    conn.close()

def cmnd_15():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (15)")
    conn.commit()
    conn.close()

def cmnd_16():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (16)")
    conn.commit()
    conn.close()

def cmnd_17():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (17)")
    conn.commit()
    conn.close()

def cmnd_18():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (18)")
    conn.commit()
    conn.close()

def cmnd_19():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (19)")
    conn.commit()
    conn.close()

def cmnd_20():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (20)")
    conn.commit()
    conn.close()

def cmnd_21():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (21)")
    conn.commit()
    conn.close()

def cmnd_22():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (22)")
    conn.commit()
    conn.close()

def cmnd_23():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (23)")
    conn.commit()
    conn.close()

def cmnd_24():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (24)")
    conn.commit()
    conn.close()

def cmnd_25():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (25)")
    conn.commit()
    conn.close()

def cmnd_26():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (26)")
    conn.commit()
    conn.close()

def cmnd_27():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (27)")
    conn.commit()
    conn.close()

def cmnd_28():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (28)")
    conn.commit()
    conn.close()

def cmnd_29():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (29)")
    conn.commit()
    conn.close()

def cmnd_30():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (30)")
    conn.commit()
    conn.close()

def cmnd_31():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (31)")
    conn.commit()
    conn.close()

def cmnd_32():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (32)")
    conn.commit()
    conn.close()

def cmnd_33():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (33)")
    conn.commit()
    conn.close()

def cmnd_34():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (34)")
    conn.commit()
    conn.close()

def cmnd_35():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (blk) VALUES (35)")
    conn.commit()
    conn.close()

def cmnd_36():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (red) VALUES (36)")
    conn.commit()
    conn.close()

def cmnd_0():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO numbers (zero) VALUES (0)")
    conn.commit()
    conn.close()

def reset():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM numbers") 
    conn.commit()
    conn.close()
   
def undo():
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM numbers WHERE rowid = (SELECT MAX(rowid) FROM numbers);") 
    conn.commit()
    conn.close()

def standard(): 
    conn=sqlite3.connect("test-numbers.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM numbers ORDER BY rowid DESC;")
    result1=cur.fetchall()
    conn.close()
    return result1

#WORKING ON PROPER OUTPUT
def update():
    tree.delete(*tree.get_children())
    for result1 in standard():
        tree.insert("",END, values=result1)
    
#BUTTON/ACTION COMMAND SECTION OF PROGRAM
b1=Button(root,text="1", width=2,command=cmnd_1) 
b1.grid(row=0,column=0)

b2=Button(root,text="2", width=2,command=cmnd_2)
b2.grid(row=1,column=0)

b3=Button(root,text="3", width=2,command=cmnd_3)
b3.grid(row=2,column=0)

b4=Button(root,text="4", width=2,command=cmnd_4)
b4.grid(row=3,column=0)

b5=Button(root,text="5", width=2,command=cmnd_5) 
b5.grid(row=4,column=0)

b6=Button(root,text="6", width=2,command=cmnd_6)
b6.grid(row=5,column=0)

b7=Button(root,text="7", width=2,command=cmnd_7)
b7.grid(row=6,column=0)

b8=Button(root,text="8", width=2,command=cmnd_8)
b8.grid(row=7,column=0)

b9=Button(root,text="9", width=2,command=cmnd_9) 
b9.grid(row=8,column=0)

b10=Button(root,text="10", width=2,command=cmnd_10)
b10.grid(row=9,column=0)

b11=Button(root,text="11", width=2,command=cmnd_11)
b11.grid(row=10,column=0)

b12=Button(root,text="12", width=2,command=cmnd_12)
b12.grid(row=11,column=0)

b13=Button(root,text="13", width=2,command=cmnd_13) 
b13.grid(row=0,column=1)

b14=Button(root,text="14", width=2,command=cmnd_14)
b14.grid(row=1,column=1)

b15=Button(root,text="15", width=2,command=cmnd_15)
b15.grid(row=2,column=1)

b16=Button(root,text="16", width=2,command=cmnd_16)
b16.grid(row=3,column=1)

b17=Button(root,text="17", width=2,command=cmnd_17) 
b17.grid(row=4,column=1)

b18=Button(root,text="18", width=2,command=cmnd_18)
b18.grid(row=5,column=1)

b19=Button(root,text="19", width=2,command=cmnd_19)
b19.grid(row=6,column=1)

b20=Button(root,text="20", width=2,command=cmnd_20)
b20.grid(row=7,column=1)

b21=Button(root,text="21", width=2,command=cmnd_21) 
b21.grid(row=8,column=1)

b22=Button(root,text="22", width=2,command=cmnd_22)
b22.grid(row=9,column=1)

b23=Button(root,text="23", width=2,command=cmnd_23)
b23.grid(row=10,column=1)

b24=Button(root,text="24", width=2,command=cmnd_24)
b24.grid(row=11,column=1)

b25=Button(root,text="25", width=2,command=cmnd_25)
b25.grid(row=0,column=2)

b26=Button(root,text="26", width=2,command=cmnd_26)
b26.grid(row=1,column=2)

b27=Button(root,text="27", width=2,command=cmnd_27)
b27.grid(row=2,column=2)

b28=Button(root,text="28", width=2,command=cmnd_28)
b28.grid(row=3,column=2)

b29=Button(root,text="29", width=2,command=cmnd_29)
b29.grid(row=4,column=2)

b30=Button(root,text="30", width=2,command=cmnd_30) 
b30.grid(row=5,column=2)

b31=Button(root,text="31", width=2,command=cmnd_31)
b31.grid(row=6,column=2)

b32=Button(root,text="32", width=2,command=cmnd_32)
b32.grid(row=7,column=2)

b33=Button(root,text="33", width=2,command=cmnd_33)
b33.grid(row=8,column=2)

b34=Button(root,text="34", width=2,command=cmnd_34)
b34.grid(row=9,column=2)

b35=Button(root,text="35", width=2,command=cmnd_35) 
b35.grid(row=10,column=2)

b36=Button(root,text="36", width=2,command=cmnd_36)
b36.grid(row=11,column=2)

b0=Button(root,text="0", width=2,command=cmnd_0)
b0.grid(row=12,column=1)

b37=Button(root,text="undo", width=4,command=undo)
b37.grid(row=13,column=0)

b38=Button(root,text="update", width=4,command=update)
b38.grid(row=13,column=1)

b39=Button(root,text="reset", width=4,command=reset)
b39.grid(row=13,column=2)

b40=Button(root,text="exit", width=4,command=root.destroy) 
b40.grid(row=14,column=0)

#CREATES THE TREEVIEW TABLE OUTPUT
tree = ttk.Treeview(show='headings', height='10')
#CREATE COLUMNS
tree["column"]=("red","zero","blk")
tree.column("red",width=50)
tree.column("zero",width=50)
tree.column("blk",width=50)

tree.heading("red",text="red")
tree.heading("zero",text="zero")
tree.heading("blk",text="blk")

tree.grid(row=15,column=3)


root.mainloop()

print("Program Executed!")
