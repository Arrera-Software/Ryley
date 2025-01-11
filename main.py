from cProfile import label

from ryley import*
from src.ryleyGUI import *



def btnVousClick():
    ryley = Ryley("fichierJSON/configNeuronVouvoiment.json")
    screen.destroy()
    ryley.bootAssistant()

def btnTuClick():
    ryley = Ryley("fichierJSON/configNeuronTutoiment.json")

    screen.destroy()
    ryley.bootAssistant()

def main():
    ryley = guiRyley("fichierJSON/configNeuronTutoiment.json")
    ryley.active()



if __name__ == "__main__":
    main()