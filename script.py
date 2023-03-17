from setting.setting import *

var = int(input("1.Parametre\n2.Touche\n0.quitter\n"))
match var :
    case 1 :
        Setting()
    case 2 :
        def anychar(event):
            print ("event.char =", event.char, "event.keysym =",event.keysym, "event.keycode =",event.keycode)
            print(event)

        Ecran = Tk()
        Ecran.bind("<Key>", anychar)
        Ecran.mainloop()
    case 0 :
        print("Ok")