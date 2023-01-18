from src.varriable import*
from tkinter import*

class ryleyRoutine :
    def __init__(self):
        self.routine = Toplevel()
        self.routine.title("Ryley : Routine")
        self.routine.maxsize(500,500)
        self.routine.minsize(500,500)
        self.routine.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.routine.config(bg=mainColor)
        
        self.labelText = Label(self.routine,text="Routine",bg=mainColor,fg=mainTextColor,font=("arial",20))
        
        self.labelText.pack()
        self.routine.mainloop()
        
        