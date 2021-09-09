from tkinter import *
from tkinter import ttk
import mysql.connector


class Formulario:
    def __init__(self, maestro):
        self.maestro = maestro
        maestro.title (" Aplicacion Formulario")
        
        #ventana
        self.maestro.geometry ("400x300+0+0")
        self.maestro.configure (bg ="#6f6fb8")
        
        ## Label's
        self.label_nombre = Label (maestro, text ="Nombre: ", font = "bold")
        self.label_nombre.place (x =10, y =50)
        self.label_nombre.configure (bg= "#6f6fb8")

        self.label_apellido = Label (maestro, text ="Apellido:", font ="bold")
        self.label_apellido.place (x =12, y =80)
        self.label_apellido.configure (bg ="#6f6fb8")
        
        self.label_telefono = Label (maestro, text ="Telefono: ", font ="Bold")
        self.label_telefono.place (x=12, y =120)
        self.label_telefono.configure (bg ="#6f6fb8")
        
        self.label_email = Label (maestro, text ="Email: ", font ="bold")
        self.label_email.place (x =12, y =150)
        self.label_email.configure (bg ="#6f6fb8")
        
        
        #Entry's
        
        self.entry_nombre = Entry (maestro)
        self.entry_nombre.place (x =120, y =50)
        
        self.entry_apellido = Entry (maestro)
        self.entry_apellido.place (x =120, y =80)

        self.entry_telefono = Entry (maestro)
        self.entry_telefono.place (x =120, y =120)
        
        self.entry_email = Entry (maestro)
        self.entry_email.place (x =120 , y =150)
        
        #buttons's
        
        self.button_edit = Button (maestro, text ="Edd", font ="bold", height =1, width =6)
        self.button_edit.place (x =12, y =250)
        
        self.button_delete = Button (maestro, text ="Delete", font ="bold", height =1, width =6)
        self.button_delete.place (x =85, y =250)
        
        self.button_quit = Button (maestro, text ="Quit", font ="bold", height =1, width =6, command = maestro.quit)
        self.button_quit.place (x =160, y =250)
        
    def add(self):  
        datos = (self.entry_nombre.get() , self.entry_apellido.get(), self.entry_email.get(), self.entry_telefono.get())
        
root = Tk()
Miformulario = Formulario (root)
root.mainloop()
