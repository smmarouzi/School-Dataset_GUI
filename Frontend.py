# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 19:02:56 2018

@author: mm
"""

from tkinter import *
import Backend
#import datetime

## Define functions
# view function
def view_command():
    list1.delete(0,END)
    for row in Backend.view():
        list1.insert(END,row)
        
# Search function
def search_command():
    list1.delete(0,END)
    for row in Backend.search(Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get()):
        list1.insert(END,row)
 
#Insert function
def add_command():  
    Backend.insert(Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get())  
    list1.delete(0,END)
    list1.insert(END,Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get())

# delet ao modify the selected line
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[8])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[9])
    e10.delete(0,END)
    e10.insert(END,selected_tuple[10])
    
def update_command():
    Backend.update(selected_tuple[0],Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get())

def delete_command():
    Backend.delete(selected_tuple[0])
# Delete items by id
#def delete_command():
#    list1.delete(0,END)
#    Backend.delete(ID_text.get())
#    list1.insert(END,ID_text.get())
#
#def update_command():
#    list1.delete(0,END)
#    Backend.update(ID_text.get(),Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get())
#    list1.insert(END,(ID_text.get(),Student_Name_text.get(),Hours_bought_text.get(),First_class_text.get(),Grade_text.get(),Subject1_text.get(),Subject2_text.get(),Subject3_text.get(),Days_of_attendace_text.get(),Hours_of_attendance_text.get(),Comments_text.get()))
    
# Close GUI
def close_window (): 
    window.destroy()
    
# Clear items]
def clear_window():
    e0.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    list1.delete(0,END)
    
#Create window object
window=Tk()

window.title("GUI")
window.geometry('480x400')

#defile ten lables Student_Name,Hours_bought,First_class,Grade,Subject1,Subject2,Subject3,Days_of_attendace,Hours_of_attendance,Comments
l0=Label(window, text="ID")
l0.grid(row=0,column=0)

l1=Label(window, text="Student_Name")
l1.grid(row=1,column=0)

l2=Label(window, text="Hours_bought")
l2.grid(row=2,column=0)

l3=Label(window, text="First_class")
l3.grid(row=3,column=0)

l4=Label(window, text="Grade")
l4.grid(row=4,column=0)

l5=Label(window, text="Subject1")
l5.grid(row=5,column=0)

l6=Label(window, text="Subject2")
l6.grid(row=6,column=0)

l7=Label(window, text="Subject3")
l7.grid(row=7,column=0)

l8=Label(window, text="Days_of_attendace")
l8.grid(row=8,column=0)

l9=Label(window, text="Hours_of_attendance")
l9.grid(row=9,column=0)

l10=Label(window, text="Comments")
l10.grid(row=10,column=0)

#define Entries
ID_text=StringVar()
e0=Entry(window,textvariable=ID_text)
e0.grid(row=0,column=1)

Student_Name_text=StringVar()
e1=Entry(window,textvariable=Student_Name_text)
e1.grid(row=1,column=1)

Hours_bought_text=StringVar()
e2=Entry(window,textvariable=Hours_bought_text)
e2.grid(row=2,column=1)

First_class_text=StringVar()
e3=Entry(window,textvariable=First_class_text)
e3.grid(row=3,column=1)

Grade_text=StringVar()
e4=Entry(window,textvariable=Grade_text)
e4.grid(row=4,column=1)

Subject1_text=StringVar()
e5=Entry(window,textvariable=Subject1_text)
e5.grid(row=5,column=1)

Subject2_text=StringVar()
e6=Entry(window,textvariable=Subject2_text)
e6.grid(row=6,column=1)

Subject3_text=StringVar()
e7=Entry(window,textvariable=Subject3_text)
e7.grid(row=7,column=1)

Days_of_attendace_text=StringVar()
e8=Entry(window,textvariable=Days_of_attendace_text)
e8.grid(row=8,column=1)

Hours_of_attendance_text=StringVar()
e9=Entry(window,textvariable=Hours_of_attendance_text)
e9.grid(row=9,column=1)

Comments_text=StringVar()
e10=Entry(window,textvariable=Comments_text)
e10.grid(row=10,column=1)

#define ListBox
list1=Listbox(window,height=6,width=60)
list1.grid(row=14,column=0,rowspan=6,columnspan=2)

#Attach scrollbar to the list
sb1=Scrollbar(window)
sb1.grid(row=14,column=3,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# Select rows in the list1
list1.bind('<<ListboxSelect>>',get_selected_row)
#define buttons
b1=Button(window, text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)
#b1.pack()

b2=Button(window, text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)
#b2.pack()

b3=Button(window, text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
#b3.pack()

b4=Button(window, text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)
#b4.pack()

b5=Button(window, text="Delet selected",width=12,command=delete_command)
b5.grid(row=6,column=3)
#b5.pack()

b6=Button(window, text="Close",width=12,command=close_window)
b6.grid(row=7,column=3)
#b6.pack()

b7=Button(window, text="Clear",width=12,command=clear_window)
b7.grid(row=8,column=3)

window.mainloop()


