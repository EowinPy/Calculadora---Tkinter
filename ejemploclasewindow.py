from tkinter import *
from tkinter import ttk


#el modulo ttk , se usa para dar mas estilo
#y brindar mas opciones al momento de configurar el elemento en el gui (aplicacion)

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.master.geometry("800x600")
        self.master.configure(bg= "#5514a7")
        

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet )  
        self.greet_button.place (x =500, y =100)
                        
                        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()