import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import *

a = tk.Tk()

a.geometry("1600x900")
a.title("ovenstory")

bg = Image.open(r"bg.jpg")
bg = ImageTk.PhotoImage(bg.resize((1550,900)))
photo = Label(a, image=bg)
photo.pack()

a.config(bg="black")

title = Label(a,text="Welcome to OvenStory 🍕",bg="black",fg="white",font=("Ink Free",40,"bold"))
title.place(x=800,y=150)

un = Label(a,text="Username 🍕",bg="black",fg="white",font=("poppins",20))
un.place(x=900,y=300)

une = Entry(a,bg="white",fg="black",font=("calibri",20))
une.place(x=900,y=350)

pw = Label(a,text="Password 🍕",bg="black",fg="white",font=("Ink Free",20))
pw.place(x=900,y=400)

pwe = Entry(a,bg="white",fg="black",font=("calibri",20),show="*")
pwe.place(x=900,y=450)
'''
def submit():
    u = une.get()
    p = str(pwe.get())
    if u=="" or p=="":
        messagebox.showerror("LOGIN", "Fill All Details")
    else:
        import pymysql as p
        db = p.connect(host="localhost",
                       user="root",
                       password="1234",
                       database="pizza")
        
        import time
        time = str(time.ctime())
        cursor = db.cursor()
        query = "Insert into login values('%s','%s','%s')"%(u,p,time)
        cursor.execute(query)
        db.commit()
        db.close()
'''
def submit():
    u = une.get()
    p = pwe.get()  # No need to wrap in str(), .get() is already a string
    
    if u == "" or p == "":
        messagebox.showerror("LOGIN", "Fill All Details")
    else:
        import pymysql as p_mysql
        import time as t_module
        
        # 1. Capture time safely without overwriting the module name
        current_time = str(t_module.ctime())
        
        try:
            db = p_mysql.connect(
                host="localhost",
                user="root",
                password="1234",
                database="pizza"
            )
            cursor = db.cursor()
            
            # 2. Use %s placeholders WITHOUT single quotes
            query = "INSERT INTO login VALUES (%s, %s, %s)"
            
            # 3. Pass data safely as a tuple
            cursor.execute(query, (u, p, current_time))
            
            db.commit()
            messagebox.showinfo("LOGIN", "Login Saved Successfully!")
            
        except Exception as e:
            if 'db' in locals():
                db.rollback()
            messagebox.showerror("Database Error", e)
            
        finally:
            if 'db' in locals():
                db.close()
                a.destroy()
                import menu
        
submit = Button(a,text="🍕 Submit 🍕",fg="black",bg="white",width=25,font=("Ink Free",15),command=submit)
submit.place(x=900,y=520)

a.mainloop()



