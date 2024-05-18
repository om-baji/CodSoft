import customtkinter as ctk
import tkinter as tk
import random
from utils import decider
from PIL import Image


app = ctk.CTk()
app.title("Rock,Paper & Scissors")
app.geometry("500x600")

def choose(user):
    options = ['Rock','Paper','Scissor']
    game = random.choice(options)
    match.configure(text="{} vs {}".format(user,game))
    if user == game :
        result.configure(text="Draw",
        text_color="White")
    else:
        res = decider(user,game)
        if res:
            result.configure(
            text="User Wins!",
            text_color="green")
            
        else :
            result.configure(
            text="Computer Wins!",
            text_color="red")
        
# sci_image = ctk.CTkImage(light_image=Image.open('rock_paper/scissor.png'),
#             dark_image=Image.open('rock_paper/scissor.png'),
#             size=(100,100)) 
# sci_label = ctk.CTkLabel(app,
#         image=sci_image,
#         text='')
# sci_label.place(x=300,y=200)

title = ctk.CTkLabel(app,
        text="Rock, Paper and Scissors!",
        font=("Roboto",24))
title.place(x=110,y=20)

rock = ctk.CTkButton(app,
        text="Rock",
        width=100,
        height=50,
        command=lambda:choose('Rock'))
rock.place(x=60,y=100)

Paper = ctk.CTkButton(app,
        text="Paper",
        width=100,
        height=50,
        command=lambda:choose('Paper'))
Paper.place(x=180,y=100)


scissors = ctk.CTkButton(app,
        text="Scissors",
        width=100,
        height=50,
        command=lambda:choose('Scissor'))
scissors.place(x=300,y=100)


match = ctk.CTkLabel(app,
        text="",
        font=("Roboto",24))
match.place(x=250,y=290,anchor=ctk.CENTER)

result = ctk.CTkLabel(app,
        text="Result",
        font=("Roboto",24))
result.place(x=250,y=390,anchor=ctk.CENTER)

app.mainloop()
