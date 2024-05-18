import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("500x600")
app.title("Todo")
app.resizable(False,False)

def add_task():
    string = entry.get() 
    if len(string)==0:
        messagebox.showerror("Error","Please enter!")     
    else :
        list_box.insert(0,string)
        entry.delete(0,"end")
    
    
def remove():
    task = list_box.curselection()
    if task:
        list_box.delete(task[0])
    else:
       messagebox.showerror("Error","Please select!")

title = ctk.CTkLabel(app,text="TO DO LIST",font=("Roboto",24))
title.place(x=200,y=20)

entry = ctk.CTkEntry(app,placeholder_text="Enter Task",
        width=300,height=55)
entry.place(x=100,y=160)

add = ctk.CTkButton(app,fg_color="orange",
        height=50,width=100,text="Add Task",command=add_task)
add.place(x=100,y=90)
rem = ctk.CTkButton(app,fg_color="orange",
        height=50,width=100,text="Remove Task",command=remove)
rem.place(x=260,y=90)

list_box = tk.Listbox(app,width=70,height=15,
            bg="#393533",font=("Roboto",10),
            foreground="white")
list_box.place(x=90,y=280)

app.mainloop()
