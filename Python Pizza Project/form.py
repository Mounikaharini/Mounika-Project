import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import *

a = tk.Tk()

a.geometry("1600x900")
a.title("ovenstory")

a.config(bg="black")

title = Label(a,text="Your Order on OvenStory 🍕",bg="black",fg="white",font=("Ink Free",40,"bold"))
title.pack()

a.mainloop()
