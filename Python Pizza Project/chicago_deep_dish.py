import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import *

a = tk.Tk()

a.geometry("1600x900")
a.title("ovenstory Chicago Deep-Dish")

a.config(bg="black")

bg = Image.open(r"1.jpg")
bg = ImageTk.PhotoImage(bg.resize((550,600)))
photo = Label(a, image=bg)
photo.place(x=100,y=120)

s1 = Label(a,text="🍕 Chicago Deep-Dish 🍕",fg="white",bg="black",font=("Ink Free",35,"bold"))
s1.pack()

s1name = Label(a,text="Name : 🍕 Chicago Deep-Dish 🍕",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
s1name.place(x=700,y=170)

t1 = """Description : A thick, square, or rectangular pie with \na spongy, bread-like crust, often topped with robust \ntomato sauce, herbs, and minimal cheese."""

s1des = Label(a,text=t1,fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
s1des.place(x=700,y=270)

s1star = Label(a,text="Price (per 1) : 🏷 Rs.680",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
s1star.place(x=700,y=440)

s1star = Label(a,text="Rating : 🌟🌟🌟🌟🌟",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
s1star.place(x=700,y=540)

s1btn = Button(a,text=" 🚚 Order Now 📦",fg="black",bg="white",width=29,font=("Comic Sans MS",15,"bold"))
s1btn.place(x=700,y=650)

a.mainloop()
