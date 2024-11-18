from cProfile import label

from ryley import*

screen = Tk()

def btnVousClick():
    ryley = Ryley("fichierJSON/configNeuronVouvoiment.json")
    screen.destroy()
    ryley.bootAssistant()

def btnTuClick():
    ryley = Ryley("fichierJSON/configNeuronTutoiment.json")

    screen.destroy()
    ryley.bootAssistant()

def main():
    screen.title("Ryley")
    screen.geometry("600x400")
    screen.resizable(False,False)
    screen.configure(bg="white")
    Label(screen,text="Voulez-vous parler à Ryley en vouvoiement ou tutoiement ?",
          bg="white",fg="black",font=("Arial","15")).pack()
    Button(screen,text="Vous",
           command=lambda : btnVousClick(),
           bg="white",fg="black",font=("Arial","15")).pack(side="right")
    Button(screen, text="Tu" ,
           command=lambda : btnTuClick(),
           bg="white",fg="black",font=("Arial","15")).pack(side="left")
    screen.mainloop()

if __name__ == "__main__":
    main()