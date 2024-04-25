import customtkinter
from utils import generate_pass

app = customtkinter.CTk()
app.geometry("400x400")
# app.iconphoto("image.png")
app.title("Random password generator")

#command
def generate_password():
    num = e1.get()
    if num.isdigit():
        length = int(num)
        if length > 15:
            disp.configure(text="Max. length is 15",text_color = "red")
        else :
            password = generate_pass(length)
            disp.configure(text=password,text_color="green")
    else :
        disp.configure(text="Invalid input",text_color="red")
    
    
# Header
title = customtkinter.CTkLabel(app,
        text="Password Generator",font=("Arial",24))
title.place(relx=0.5,rely=0.1,
            anchor=customtkinter.CENTER)

#1st entry
label1 = customtkinter.CTkLabel(app,text="Length of password : ")
label1.place(relx=0.25,rely=0.35,anchor=customtkinter.CENTER)

e1 = customtkinter.CTkEntry(app,width=100)
e1.place(relx=0.55,rely=0.35,anchor=customtkinter.CENTER)

e1_num = e1.get()

# display
disp = customtkinter.CTkLabel(app,text="",
        font=("Roboto",18))
disp.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(app,text="Generate",
        width= 100,height=30 ,hover=True,command=generate_password)
button.place(relx=0.5,rely=0.6,anchor=customtkinter.CENTER)

app.mainloop()