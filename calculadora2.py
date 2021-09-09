from tkinter import *
import tkinter as tk



calculadora = Tk()

#FRAME
calculadora.title ("Calculadora")
calculadora.geometry ("500x250")


#BOTONES

boton1 = Button (calculadora, text  ="1", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="5", column ="0", padx =2, pady =2)
boton2 = Button (calculadora, text  ="2", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="5", column ="1",padx =2, pady =2)
boton3 = Button (calculadora, text  ="3", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="5", column ="2",padx =2, pady =2)
boton4 = Button (calculadora, text  ="4", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="6", column ="0",padx =2, pady =2)
boton5 = Button (calculadora, text  ="5", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="6", column ="1",padx =2, pady =2)
boton6 = Button (calculadora, text  ="6", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="6", column ="2",padx =2, pady =2)
boton7 = Button (calculadora, text ="7", font ="bold",  borderwidth=3, height =1, width =6).grid ( row ="7", column ="0", padx =2, pady =2)
boton8 = Button (calculadora, text ="8", font ="bold",  borderwidth=3, height =1, width =6).grid ( row ="7", column = "1", padx =2, pady =2)
botton9 = Button (calculadora, text ="9", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="7", column ="2", padx =2, pady =2)
boton10 = Button (calculadora, text ="0", font ="bold", borderwidth=3, height =1, width =6).grid ( row = "8", column ="0", padx =2, pady =2)
boton11 = Button (calculadora, text =".", font ="bold", borderwidth=3, height =1, width =6).grid ( row = "8", column ="1", padx =2, pady =2)
boton12 = Button (calculadora, text ="÷", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="5", column ="3", padx =2, pady =2)
boton13 = Button (calculadora, text ="x", font ="bold", borderwidth=3, height =1, width =6).grid ( row = "6", column ="3", padx =2, pady =2)
boton14 = Button (calculadora, text ="-", font ="bold", borderwidth=3, height =1, width =6).grid ( row = "7", column ="3", padx =2, pady =2)
boton15 = Button (calculadora, text ="+", font ="bold", borderwidth=3, height =1, width =6).grid ( row = "8", column ="3", padx =2, pady =2)
boton16 = Button (calculadora, text ="=", font ="bold", borderwidth=3, height =1, width =6).grid ( row ="8", column ="2", padx =2, pady =2)

#ENTRADA

entrada = Entry (calculadora, font ="Arial 15", bd ="4", justify ="right").place (x =5, y =5)

calculadora.mainloop()