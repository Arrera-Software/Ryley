def ViewBTN(btn1,btn2,btn3,btn4):
    btn1.place(x=20,y=70)
    btn2.place(x=20,y=140)
    btn3.place(x=20,y=210)
    btn4.place(x=20,y=280)
    
def NoViewBTN(btn1,btn2,btn3,btn4):
    btn1.place_forget()
    btn2.place_forget()
    btn3.place_forget()
    btn4.place_forget()