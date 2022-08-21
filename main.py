from tkinter import*
import webbrowser
import os
import datetime
import random
import requests
from tkinter.messagebox import showinfo
from translate import translate
import time

screen = Tk()
def Meteo():
    print("Okkkkk")
screen.title("Ryley")
screen.maxsize(500,700)
screen.minsize(500,700)
screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
B1 = Button (text="meteo",command=Meteo).pack
screen.mainloop()