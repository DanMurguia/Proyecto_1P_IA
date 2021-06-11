from tkinter import *
import tkinter as tk
from tkinter import filedialog
import dibujo_estrella

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("MINTRIS")
        self.parent.geometry("500x500")
        self.configure(bg='#6B0002')


    
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)        
        
        btn_Descifrar = tk.Button(self, text="Jugar", 
                               bg='#4B7D23',width=10,height = 5, command=self.jugar,
                               foreground='white',font=('Arial',50,'bold italic'))
        btn_Descifrar.grid(row=1,column=1,pady=20)
        
        
    def jugar(self):
        dibujo_estrella.dibujar()
        
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
