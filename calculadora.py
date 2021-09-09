from tkinter import *
from math import *



calculadora = Tk()

calculadora.title ("Calculadora")#titulo de ventana
calculadora.geometry ("320x300") #tamaño de la ventana
calculadora.resizable(0,0) # evitar cambiar tamaño

operador =""
input_text =StringVar()

#ENTRADA

datos = Entry (calculadora, font = "Arial,25", bd ="3", justify ="right", width =26, textvariable =input_text).place (x =35, y= 10 )
    

#funciones    
def digito (num):
    global operador
    operador = operador+str(num)
    input_text.set (operador)


def limpiar():
    global operador
    operador = ("")
    input_text.set ("0")

def operacion():
    global operador
    try:
        opera = str(eval (operador))
    except:
        limpiar()
        opera = ("Error")
        input_text.set(opera)
        

#BOTONES

boton1 = Button (calculadora, text  ="1", font ="bold",borderwidth=3, height =1, width =6, command = lambda :digito (1)).place (x =20, y =130)
boton2 = Button (calculadora, text  ="2", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (2)).place (x =90, y =130)
boton3 = Button (calculadora, text  ="3", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (3)).place (x =160, y =130)
boton4 = Button (calculadora, text  ="4", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (4)).place (x =20, y =90)
boton5 = Button (calculadora, text  ="5", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (5)).place (x =90, y =90)
boton6 = Button (calculadora, text  ="6", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (6)).place (x =160, y =90)
boton7 = Button (calculadora, text  ="7", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (7)).place (x =20, y =50)
boton8 = Button (calculadora, text  ="8", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (8)).place (x =90, y =50)
boton9 = Button (calculadora, text  ="9", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (9)).place (x =160, y =50)
boton10 = Button (calculadora, text  ="0", font ="bold", borderwidth=3, height =1, width =6, command = lambda :digito (0)).place (x =90, y =170)
boton11 = Button (calculadora, text =".", font = "bold", borderwidth =3, height =1, width =6, command = lambda :digito (".")).place (x =160, y =170)
boton12 = Button (calculadora, text ="+", font ="bold", borderwidth =3, height =1, width =6, command = lambda :digito ("+")).place (x =20, y =170)
boton13 = Button (calculadora, text ="/", font = "bold", borderwidth =3, height =1, width =6, command = lambda :digito ("/")).place (x =230, y =50)
boton14 = Button (calculadora, text ="X", font ="bold", borderwidth =3, height =1, width =6, command = lambda :digito ("x")).place (x =230, y =90)
boton15 = Button (calculadora, text ="-", font ="bold", borderwidth =3, height =1, width =6, command = lambda :digito ("-")).place (x =230, y =130)
boton16 = Button (calculadora, text ="=", font ="bold", borderwidth =3, height =1, width =6, command = operacion).place (x =230, y =170)
boton17 = Button (calculadora, text ="Limpiar", font ="bold", borderwidth =3, height =1, width =6, command = limpiar).place (x =20, y =210)



calculadora.mainloop()

