#Importar libreries
import ttkbootstrap as bootstrap
import tkinter as tk
from tkinter import ttk, messagebox

#Crear finestra
#sex
class App(tk.Frame):
    def __init__(self, w):
        super().__init__(w)
        self.w = w
        self.w.title("CalcLife")
        self.__create_elements()

    ####################
    # CREACIÓ DE WIDGETS
    ####################
    def __create_elements(self):
        #INPUT DE DINERS TOTALS I SALARI
        self.lbl_mainTitle = ttk.Label(self, text="CalcLIFE", font=("Arial", 30,"bold"), padding=20)
        self.lbl_mainTitle.grid(row=0, column=0, columnspan=2, pady=20)

        #self.lbl_title = ttk.Label(self, text="Introduce los datos:", font=("Arial", 20))
        #self.lbl_title.pack()

        #FRAME DE INPUT
        self.frm_input = ttk.Frame(self)

        self.lbl_total = ttk.Label(self.frm_input, text="Dinero total:", font=("Arial", 15))
        self.lbl_total.grid(row=0, column=0)
        self.ent_total = ttk.Entry(self.frm_input, font=("Arial", 15))
        self.ent_total.grid(row=1, column=0, padx=10, pady=10)

        self.lbl_salario = ttk.Label(self.frm_input, text="Salario:", font=("Arial", 15))
        self.lbl_salario.grid(row=0, column=1)
        self.ent_salario = ttk.Entry(self.frm_input, font=("Arial", 15))
        self.ent_salario.grid(row=1, column=1)

        self.frm_input.grid(row=1, column=0, columnspan=2, pady=10)

        self.btt_calcular = ttk.Button(self, text="Calcular", command=lambda:self.calcular(), width=20)
        self.btt_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        #OUTPUT TOTAL DE DINERS
    
        #FRAME DE OUTPUT
        self.frm_ouput = ttk.Frame(self,borderwidth=2, relief="solid")


        self.lbl_resumen_total = ttk.Label(self.frm_ouput, text="Resumen total:", font=("Arial", 20),padding=10)
        self.lbl_resumen_total.grid(row=0, column=0)

        # TOTAL - CASA
        self.lbl_total_casa = ttk.Label(self.frm_ouput, text="40""%"" Casa:", font=("Arial", 13))
        self.lbl_total_casa.grid(row=1, column=0)
        self.lbl_total_casa_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_total_casa_res.grid(row=2, column=0)

        # TOTAL - AHORRO
        self.lbl_total_ahorro = ttk.Label(self.frm_ouput, text="10""%"" Ahorro:", font=("Arial", 13))
        self.lbl_total_ahorro.grid(row=3, column=0)
        self.lbl_total_ahorro_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_total_ahorro_res.grid(row=4, column=0)

        # TOTAL - COCHE
        self.lbl_total_coche = ttk.Label(self.frm_ouput, text="10""%"" Coche:", font=("Arial", 13))
        self.lbl_total_coche.grid(row=5, column=0)
        self.lbl_total_coche_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_total_coche_res.grid(row=6, column=0)

        # TOTAL - CAPRICHOS
        self.lbl_total_caprichos = ttk.Label(self.frm_ouput, text="10""%"" Caprichos:", font=("Arial", 13))
        self.lbl_total_caprichos.grid(row=7, column=0)
        self.lbl_total_caprichos_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_total_caprichos_res.grid(row=8, column=0)

        # TOTAL - LIFE
        self.lbl_total_life = ttk.Label(self.frm_ouput, text="30""%"" Life:", font=("Arial", 13))
        self.lbl_total_life.grid(row=9, column=0)
        self.lbl_total_life_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_total_life_res.grid(row=10, column=0)

        #RESUMEN INGRESOS DEL SALARI
        self.lbl_resumen_ingresos = ttk.Label(self.frm_ouput, text="Resumen ingresos:", font=("Arial", 20))
        self.lbl_resumen_ingresos.grid(row=0, column=1)

        # SALARI - CASA
        self.lbl_ingresos_casa = ttk.Label(self.frm_ouput, text="40""%"" Casa:", font=("Arial", 13))
        self.lbl_ingresos_casa.grid(row=1, column=1)
        self.lbl_ingresos_casa_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_ingresos_casa_res.grid(row=2, column=1)

        # SALARI - AHORRO
        self.lbl_ingresos_ahorro = ttk.Label(self.frm_ouput, text="10""%"" Ahorro:", font=("Arial", 13))
        self.lbl_ingresos_ahorro.grid(row=3, column=1)
        self.lbl_ingresos_ahorro_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_ingresos_ahorro_res.grid(row=4, column=1)

        # SALARI - COCHE
        self.lbl_ingresos_coche = ttk.Label(self.frm_ouput, text="10""%"" Coche:", font=("Arial", 13))
        self.lbl_ingresos_coche.grid(row=5, column=1)
        self.lbl_ingresos_coche_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_ingresos_coche_res.grid(row=6, column=1)

        # SALARI - CAPRICHOS
        self.lbl_ingresos_caprichos = ttk.Label(self.frm_ouput, text="10""%"" Caprichos:", font=("Arial", 13))
        self.lbl_ingresos_caprichos.grid(row=7, column=1)
        self.lbl_ingresos_caprichos_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_ingresos_caprichos_res.grid(row=8, column=1)

        # SALARI - LIFE
        self.lbl_ingresos_life = ttk.Label(self.frm_ouput, text="30""%"" Life:", font=("Arial", 13))
        self.lbl_ingresos_life.grid(row=9, column=1)
        self.lbl_ingresos_life_res = ttk.Label(self.frm_ouput, text="0", font=("Arial", 13))
        self.lbl_ingresos_life_res.grid(row=10, column=1)


        self.frm_ouput.grid(row=3, column=0, columnspan=2, pady=10)

    #########
    #FUNCIONS
    #########
    def calcular(self):
        try:
            total = self.ent_total.get()
            salario = self.ent_salario.get()

            total = float(total) if total else None
            salario = float(salario) if salario else None

            if total is None and salario is None:
                raise ValueError("Has de plenar al menys un camp")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Aquesta entrada no és vàlida: {e}")
            return
        
        # Si total no es None (hi ha data al input) actualitzem els labels
        if total is not None:
            self.lbl_total_casa_res.config(text=f"{total * 0.4:.2f}")
            self.lbl_total_ahorro_res.config(text=f"{total * 0.1:.2f}")
            self.lbl_total_coche_res.config(text=f"{total * 0.1:.2f}")
            self.lbl_total_caprichos_res.config(text=f"{total * 0.1:.2f}")
            self.lbl_total_life_res.config(text=f"{total * 0.3:.2f}")
         # Del contrari, posem tots els labels a 0 ja que no hi han dades i així evitem errors
        else:
            self.lbl_total_casa_res.config(text="0")
            self.lbl_total_ahorro_res.config(text="0")
            self.lbl_total_coche_res.config(text="0")
            self.lbl_total_caprichos_res.config(text="0")
            self.lbl_total_life_res.config(text="0")

        # Seguimn el mateix procediment condicional que a dalt
        if salario is not None:
            self.lbl_ingresos_casa_res.config(text=f"{salario * 0.4:.2f}")
            self.lbl_ingresos_ahorro_res.config(text=f"{salario * 0.1:.2f}")
            self.lbl_ingresos_coche_res.config(text=f"{salario * 0.1:.2f}")
            self.lbl_ingresos_caprichos_res.config(text=f"{salario * 0.1:.2f}")
            self.lbl_ingresos_life_res.config(text=f"{salario * 0.3:.2f}")
        else:
            self.lbl_ingresos_casa_res.config(text="0")
            self.lbl_ingresos_ahorro_res.config(text="0")
            self.lbl_ingresos_coche_res.config(text="0")
            self.lbl_ingresos_caprichos_res.config(text="0")
            self.lbl_ingresos_life_res.config(text="0")




w = tk.Tk()
w.geometry("500x600")
app = App(w)
app.pack(fill="both", expand="True")
app.mainloop()