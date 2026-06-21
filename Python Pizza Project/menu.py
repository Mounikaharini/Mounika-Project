import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import *

a = tk.Tk()

a.geometry("1600x900")
a.title("ovenstory")

a.config(bg="black")

title = Label(a,text="OUR MENU 🍕",bg="black",fg="white",font=("Ink Free",40,"bold"))
title.pack()

def product(name,img,price):

    a = tk.Tk()

    a.geometry("1600x900")
    a.title("ovenstory sicilian")

    a.config(bg="black")

    bg = Image.open(img)
    bg = ImageTk.PhotoImage(bg.resize((550,430)))
    photo = Label(a, image=bg)
    photo.place(x=100,y=270)

    def menu():
        a.destroy()
        import menu
    home = Button(a,text="🛎 Back to Menu",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=menu)
    home.place(x=100,y=170)

    s1 = Label(a,text=name,fg="white",bg="black",font=("Ink Free",35,"bold"))
    s1.pack()

    s1name = Label(a,text=f"Name : {name}",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
    s1name.place(x=700,y=170)

    t1 = """Description : A thick, square, or rectangular pie with \na spongy, bread-like crust, often topped with robust \ntomato sauce, herbs, and minimal cheese."""

    s1des = Label(a,text=t1,fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
    s1des.place(x=700,y=270)

    s1star = Label(a,text=f"Price (per 1) : 🏷 Rs.{price}",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
    s1star.place(x=700,y=440)

    s1star = Label(a,text="Rating : 🌟🌟🌟🌟🌟",fg="white",bg="black",font=("Comic Sans MS",20,"bold"))
    s1star.place(x=700,y=540)

    def order():
        a.destroy()
        import order

    s1btn = Button(a,text=" 🚚 Order Now 📦",fg="black",bg="white",width=29,font=("Comic Sans MS",15,"bold"),command=order)
    s1btn.place(x=700,y=650)

    a.mainloop()
    
bg = Image.open(r"6.jpg")
bg = ImageTk.PhotoImage(bg.resize((350,230)))
photo = Label(a, image=bg)
photo.place(x=100,y=120)

def s1():
    a.destroy()
    name = "🍕 Sicilian Pizza 🍕"
    img = r"6.jpg"
    price = 580
    product(name,img,price)
    
s1 = Button(a,text="🍕 Sicilian 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s1)
s1.place(x=100,y=370)

bg1 = Image.open(r"1.jpg")
bg1 = ImageTk.PhotoImage(bg1.resize((350,230)))
photo1 = Label(a, image=bg1)
photo1.place(x=600,y=120)

def s2():
    a.destroy()
    name = "🍕 Chicago Deep-Dish 🍕"
    img = r"1.jpg"
    price = 630
    product(name,img,price)
    
s2 = Button(a,text="🍕 Chicago Deep-Dish 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s2)
s2.place(x=600,y=370)

bg2 = Image.open(r"2.jpg")
bg2 = ImageTk.PhotoImage(bg2.resize((350,230)))
photo2 = Label(a, image=bg2)
photo2.place(x=1100,y=120)

def s3():
    a.destroy()
    name = "🍕 Margherita 🍕"
    img = r"2.jpg"
    price = 630
    product(name,img,price)
s3 = Button(a,text="🍕 Margherita 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s3)
s3.place(x=1100,y=370)

bg3 = Image.open(r"3.jpg")
bg3 = ImageTk.PhotoImage(bg3.resize((350,230)))
photo3 = Label(a, image=bg3)
photo3.place(x=100,y=450)

def s4():
    a.destroy()
    name = "🍕 Pepperoni 🍕"
    img = r"3.jpg"
    price = 520
    product(name,img,price)
    
s4 = Button(a,text="🍕 Pepperoni 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s4)
s4.place(x=100,y=700)

bg4 = Image.open(r"4.jpg")
bg4 = ImageTk.PhotoImage(bg4.resize((350,230)))
photo4 = Label(a, image=bg4)
photo4.place(x=600,y=450)

def s5():
    a.destroy()
    name = "🍕 Quattro Formaggi 🍕"
    img = r"4.jpg"
    price = 360
    product(name,img,price)
    
s5 = Button(a,text="🍕 Quattro Formaggi 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s5)
s5.place(x=600,y=700)

bg5 = Image.open(r"5.jpg")
bg5 = ImageTk.PhotoImage(bg5.resize((350,230)))
photo5 = Label(a, image=bg5)
photo5.place(x=1100,y=450)

def s6():
    a.destroy()
    name = "🍕 Neapolitan 🍕"
    img = r"5.jpg"
    price = 920
    product(name,img,price)
    
s6 = Button(a,text="🍕 Neapolitan 🍕",fg="black",bg="white",width=29,font=("Ink Free",15,"bold"),command=s6)
s6.place(x=1100,y=700)


a.mainloop()
