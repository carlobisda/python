#qPomodoro | v1.0.0 | MIT | Carlo Bisda
#a simple Pomodoro timer that utlizes default Windows voice
#to guide you in your studies
import tkinter
from tkinter import * 
from tkinter.messagebox import *
from tkinter.filedialog import *
import win32com.client
import schedule
import datetime
import time
import os

#FUNCTION CODE BLOCK
#ACTIVATES THE TIMER LOOP
def startPom():
    schedule.clear()
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Pomodoro Timer begins in 3, 2, 1")
    schedule.every(25).minutes.do(startPomEnd)
    while True:
        schedule.run_pending()
        time.sleep(1)

def startPomEnd():
    schedule.clear()
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Work time over, 5 minute break")
    schedule.every(4).minutes.do(breakOver)
    while True:
        schedule.run_pending()
        time.sleep(1)

def breakOver():
    schedule.clear()
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("Break over, work timer starting soon.")
    schedule.every(1).minutes.do(startPom)
    while True:
        schedule.run_pending()
        time.sleep(1)


#GUI CODE BLOCK
pomoWin=Tk()
pomoWin.wm_title("qPomodoro Timer")

pw1=Button(pomoWin, text="Start Pomodoro", command=startPom)
pw1.grid(row=0, column=0)

pomoWin.mainloop()
