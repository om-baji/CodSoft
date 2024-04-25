import customtkinter
app = customtkinter.CTk()

app.geometry("500x500")
app.title("Calculator!")
app.resizable(False,False)


calculation = ""

def to_calc(symbol):
    global calculation
    calculation += str(symbol)
    e1.delete(0,"end")
    e1.insert(0,calculation)
    
def evaluate_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        e1.delete(0,"end")
        e1.insert(0,calculation)
        rs.configure(text=calculation)
    except:
        clear()
        e1.insert(0,"Error!")
        
def clear():
    global calculation
    calculation = ""
    e1.delete(0,"end")
    e1.insert(0,calculation)
    rs.configure(text="Result")
    
#top line
e1 = customtkinter.CTkEntry(app,placeholder_text="Enter",
  width=500,height=50)
e1.place(relx=0.5,rely=0.1,anchor=customtkinter.CENTER)
e1.get()

rs = customtkinter.CTkLabel(app,text="Result",
  width=500,height=50)
rs.place(relx=0.5,rely=0.2,anchor=customtkinter.CENTER)


# Number buttons
one = customtkinter.CTkButton(app,text="1",
    width=120,height=50,command=lambda:to_calc(1))
one.place(relx=0.15,rely=0.35,anchor=customtkinter.CENTER)
two = customtkinter.CTkButton(app,text="2",
    width=120,height=50,command=lambda:to_calc(2))
two.place(relx=0.40,rely=0.35,anchor=customtkinter.CENTER)
three = customtkinter.CTkButton(app,text="3",
    width=120,height=50,command=lambda:to_calc(3))
three.place(relx=0.65,rely=0.35,anchor=customtkinter.CENTER)
plus = customtkinter.CTkButton(app,text="+",
    width=120,height=50,command=lambda:to_calc("+"))
plus.place(relx=0.9,rely=0.35,anchor=customtkinter.CENTER)


four = customtkinter.CTkButton(app,text="4",
    width=120,height=50,command=lambda:to_calc(4))
four.place(relx=0.15,rely=0.48,anchor=customtkinter.CENTER)
five = customtkinter.CTkButton(app,text="5",
    width=120,height=50,command=lambda:to_calc(5))
five.place(relx=0.40,rely=0.48,anchor=customtkinter.CENTER)
six = customtkinter.CTkButton(app,text="6",
    width=120,height=50,command=lambda:to_calc(6))
six.place(relx=0.65,rely=0.48,anchor=customtkinter.CENTER)
sub = customtkinter.CTkButton(app,text="-",
    width=120,height=50,command=lambda:to_calc("-"))
sub.place(relx=0.9,rely=0.48,anchor=customtkinter.CENTER)


seven = customtkinter.CTkButton(app,text="7",
    width=120,height=50,command=lambda:to_calc(7))
seven.place(relx=0.15,rely=0.6,anchor=customtkinter.CENTER)
eight = customtkinter.CTkButton(app,text="8",
    width=120,height=50,command=lambda:to_calc(8))
eight.place(relx=0.40,rely=0.6,anchor=customtkinter.CENTER)
nine = customtkinter.CTkButton(app,text="9",
    width=120,height=50,command=lambda:to_calc(9))
nine.place(relx=0.65,rely=0.6,anchor=customtkinter.CENTER)
sub = customtkinter.CTkButton(app,text="x",
    width=120,height=50,command=lambda:to_calc("*"))
sub.place(relx=0.9,rely=0.6,anchor=customtkinter.CENTER)


p1 = customtkinter.CTkButton(app,text="(",
    width=120,height=50,command=lambda:to_calc("("))
p1.place(relx=0.15,rely=0.72,anchor=customtkinter.CENTER)
zero = customtkinter.CTkButton(app,text="0",
    width=120,height=50,command=lambda:to_calc(0))
zero.place(relx=0.40,rely=0.72,anchor=customtkinter.CENTER)
p2 = customtkinter.CTkButton(app,text=")",
    width=120,height=50,command=lambda:to_calc(")"))
p2.place(relx=0.65,rely=0.72,anchor=customtkinter.CENTER)
div = customtkinter.CTkButton(app,text="/",
    width=120,height=50,command=lambda:to_calc("/"))
div.place(relx=0.9,rely=0.72,anchor=customtkinter.CENTER)


clear = customtkinter.CTkButton(app,text="Clear",
    width=200,height=50,command=clear)
clear.place(relx=0.28,rely=0.84,anchor=customtkinter.CENTER)
Equal = customtkinter.CTkButton(app,text="=",
    width=200,height=50,command=evaluate_calc)
Equal.place(relx=0.7,rely=0.84,anchor=customtkinter.CENTER)


app.mainloop()


