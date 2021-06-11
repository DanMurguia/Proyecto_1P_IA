from tkinter import *
import tkinter as tk
from tkinter import filedialog
import menu2 


class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("MINTRIS")
        self.parent.geometry("500x500")
        self.configure(bg='#6B0002')
        self.var_ente = IntVar()
        self.var_modo = IntVar()

    
        lbl = tk.Label(self, text="M I N T R I S",font=('Arial',32,'bold italic')
                        ,background='#6B0002', foreground = '#91722F')
        lbl.grid(row=0,column=0,columnspan=4, padx=90, pady=15)        
        
        lblmod = tk.Label(self, text="Seleccione un personaje",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=1,column=0,columnspan=3,padx =10 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Humano', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad0.grid(row=2, column=0)
        
        rad1 = Radiobutton(self,text='Mono', value=3,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad1.grid(row=2, column=1) 
        
        rad2 = Radiobutton(self,text='Pulpo', value=2,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad2.grid(row=2, column=2)

        rad3 = Radiobutton(self,text='Sasquach', value=4,
                           font=('Arial',14,'bold italic'),
                           background='#6B0002',foreground = '#968118',variable=self.var_ente)
        rad3.grid(row=3, column=1, pady=15)
        
                
        lblmod = tk.Label(self, text="Seleccione un modo",
                         font=('Arial',18,'bold italic')
                        ,background='#6B0002', foreground = '#04D14C')
        lblmod.grid(row=4,column=0,columnspan=3 ,pady=15)
        
        
        rad0 = Radiobutton(self,text='Manual', value=1,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad0.grid(row=5, column=0)
        
        rad1 = Radiobutton(self,text='Profundidad', value=2,
                           font=('Arial',12,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad1.grid(row=5, column=1)
        
        rad2 = Radiobutton(self,text='Anchura', value=3,
                           font=('Arial',12,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad2.grid(row=5, column=2)
        
        rad3 = Radiobutton(self,text='A*', value=4,
                           font=('Arial',14,'bold italic'), 
                           background='#6B0002',foreground = '#968118',variable=self.var_modo)
        rad3.grid(row=6, column=1)
        
        
        btn_Descifrar = tk.Button(self, text="Siguiente", 
                               bg='#4B7D23',width=10,height = 2, command=self.siguiente,
                               foreground='white',font=('Arial',10,'bold italic'))
        btn_Descifrar.grid(row=7,column=1,pady=20)
        
        
    def siguiente(self):
        ente = self.var_ente.get()
        modo = self.var_modo.get()
        parametros_inicio = {}
        if ente and modo:
            parametros_inicio['ente']=ente
            parametros_inicio['modo']=modo
            menu2.Menu2(self.parent,parametros_inicio)
        else:
            messagebox.showinfo(message="Seleccione un personaje y un modo")
        

        
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
