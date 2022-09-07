import calendar
from doctest import master
from email.policy import default
from optparse import Option
import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator
from tkinter import ttk

#create window
gui=Tk()

#open settings file
sf=open("settings.config","w")
gui.title("Free Dates")
gui.geometry("400x500")

#number of dates that the user wants to select
d_num_label=tk.Label(text="Number of dates to be selected:")
d_num_box=Spinbox(gui,from_=1,to=100,width=5) 

#date format
delimeter="/" #include option to swap for "-" or anything else if possible
d=delimeter
d_selected=tk.StringVar()
d_selected.set(d)
d_list=["/","-"]
#f_list=["14"+d+"09"+d+"2022","09"+d+"14"+d+"2022","2022"+d+"09"+d+"14","14"+d+"09"+d+"22","09"+d+"14"+d+"22","22"+d+"09"+d+"14"]
f_list=["dd"+d+"mm"+d+"yyyy","mm"+d+"dd"+d+"yyyy","yyyy"+d+"mm"+d+"dd","dd"+d+"mm"+d+"yy","mm"+d+"dd"+d+"yy","yy"+d+"mm"+d+"dd"]
f_selected=tk.StringVar()
f_selected.set(f_list[0])
d_format_label=tk.Label(text="Date format:")
d_format_box=OptionMenu(master,f_selected,f_selected,*f_list)
delimeter_label=tk.Label(text="Delimeter:")
delimeter_box=tk.OptionMenu(master,d_selected,d_selected,*d_list)
#confirm settings
def s_confirm(f):
    d_format=f
    d_num=d_num_box.get()
    delimeter=d_selected.get()
    print(d_format)
    print(d_num)
    print(delimeter)
c_button=tk.Button(master,text="Confirm",command=lambda: s_confirm(f_selected.get()))

#place date number settings
d_num_label.grid(row=0,column=0,columnspan=2)
d_num_box.grid(row=0,column=2)

#place format options
d_format_label.grid(row=1,column=0)
d_format_box.grid(row=1,column=1)
delimeter_label.grid(row=1,column=2)
delimeter_box.grid(row=1,column=3)

#place confirm button
c_button.grid(row=4,column=0)

separator = ttk.Separator(gui,orient='horizontal')
separator.place(relx=0,rely=0.47,relwidth=1, relheight=1)

if __name__ == "__main__" :
    gui.mainloop()