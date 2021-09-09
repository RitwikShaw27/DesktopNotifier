from win10toast import ToastNotifier
import time
from tkinter import *
toaster = ToastNotifier()

def rem(): 
  
    print("Setting up reminder..")
    time.sleep(1)
    print("all set!")
    time.sleep(timevalue.get()*60)
    toaster.show_toast(f"{titlevalue.get()}",
                       f"{messagevalue.get()}",
                       duration=10,
                       threaded=True)
    while toaster.notification_active(): time.sleep(0.005)
root = Tk()
root.geometry("655x333")

title = Label(root, text="Title of reminder:")
message = Label(root, text="Message of reminder:")
tim = Label(root, text="Enter in how many minutes do you want the reminder?")
title.grid()
message.grid(row=2)
tim.grid(row=3)

titlevalue = StringVar()
messagevalue = StringVar()
timevalue = DoubleVar()

titleentry = Entry(root, textvariable = titlevalue)
messageentry = Entry(root, textvariable = messagevalue)
timentry = Entry(root, textvariable = timevalue)

titleentry.grid(row=0, column=1)
messageentry.grid(row=2, column=1)
timentry.grid(row=3, column=1)

Button(fg='black', bg='yellow',text="Submit", command=rem).grid()

root.mainloop()



