from tkinter import *

def Touche(fenetre,fonc,touche):
    def anychar(event):
        if event.keycode == touche:
            fonc()               
    fenetre.bind("<Key>", anychar)