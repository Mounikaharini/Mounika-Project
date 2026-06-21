import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import *
from tkinter.ttk import Combobox
a = tk.Tk()

a.geometry("1600x900")
a.title("ovenstory")

bg = Image.open(r"orderbg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1550,800)))
photo = Label(a, image=bg)
photo.pack()

title = Label(a,text="Order Your Pizza 🍕",bg="#101010",fg="white",font=("Ink Free",30,"bold"))
title.place(x=950,y=100)

un = Label(a,text="Name 🍕",bg="black",fg="white",font=("Ink Free",15))
un.place(x=950,y=200)

une = Entry(a,bg="white",fg="black",font=("calibri",15))
une.place(x=950,y=250)

mo = Label(a,text="Mobile Number 🍕",bg="black",fg="white",font=("Ink Free",15))
mo.place(x=950,y=300)

moe = Entry(a,bg="white",fg="black",font=("calibri",15))
moe.place(x=950,y=350)

ad = Label(a,text="Address 🍕",bg="black",fg="white",font=("Ink Free",15))
ad.place(x=950,y=400)

ade = Entry(a,bg="white",fg="black",font=("calibri",15))
ade.place(x=950,y=450)

pit = Label(a, text="Select Pizza", font=("Ink Free",15), bg="black", fg="white")
pit.place(x=950, y=500)

pite=Combobox(a,width=20,font=("calibri", 15))
pite["values"]=("select Pizza","Sicilian Pizza","Chicago Deep-Dish","Margherita","Pepperoni","Quattro Formaggi","Neapolitan")
pite.current(0)
pite.place(x=950,y=550)

q = Label(a,text="Quantity 🍕",bg="black",fg="white",font=("Ink Free",15))
q.place(x=950,y=600)

qe = Entry(a,bg="white",fg="black",font=("calibri",15))
qe.place(x=950,y=650)

def bill():
    name = une.get()
    number = moe.get()
    address = ade.get()
    pizza = pite.get()
    quantity = int(qe.get())
    bill = quantity * 520

    if name=="" or number =="" or address =="" or pizza=="":
        messagebox.showerror("ORDER BILL", "Fill all details")
    elif not(number.isdigit()) or len(number)!=10:
        messagebox.showerror("ORDER BILL", "Enter The Valid Phone Number")
    elif quantity == 0:
        messagebox.showerror("ORDER BILL", "Enter The Quantity")
    else:
        final =f"""
Customer Name : {name}
Customer Mobile Number : {number}
Customer Address : {address}
Selected Pizza : {pizza}
Total Quantity : {quantity}
------------------------------------------
Total Amount To Pay : {bill}
------------------------------------------
"""
        messagebox.showinfo("ORDER BILL", final)
        import pymysql as p
        db = p.connect(host="localhost",
                       user="root",
                       password="1234",
                       database="pizza")
        cursor = db.cursor()
        query = "Insert into placedOrder values('%s','%s','%s','%s','%d','%d')"%(name,number,address,pizza,quantity,bill)
        cursor.execute(query)
        db.commit()
        db.close()
        l = Label(a,text="🍕 Order Placed 🍕",fg="black",bg="white",font=("Ink Free",15))
        l.place(x=950,y=700)
    
    
submit = Button(a,text="🍕 Buy Now 🍕",fg="black",bg="white",width=20,font=("Ink Free",15),command=bill)
submit.place(x=950,y=700)
a.mainloop()
