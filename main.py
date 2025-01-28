#Importar libreries
import ttkbootstrap as bootstrap
import tkinter as tk
from tkinter import ttk

#Crear finestra
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
        self.lbl_title = ttk.Label(self, text="INTRODUCE LOS DATOS:", font=("Arial", 20))
        self.lbl_title.pack()

        self.lbl_total = ttk.Label(self, text="Dinero total:", font=("Arial", 15))
        self.lbl_total.pack()
        self.ent_total = ttk.Entry(self, font=("Arial", 15))
        self.ent_total.pack()

        self.lbl_salario = ttk.Label(self, text="Salario:", font=("Arial", 15))
        self.lbl_salario.pack()
        self.ent_salario = ttk.Entry(self, font=("Arial", 15))
        self.ent_salario.pack()

        self.btt_calcular = ttk.Button(self, text="Calcular", command=lambda:self.calcular(), width=20)
        self.btt_calcular.pack()

        #RESUMEN TOTAL DE DINERS
        self.lbl_resumen_total = ttk.Label(self, text="Resumen total:", font=("Arial", 20))
        self.lbl_resumen_total.pack()

        # TOTAL - CASA
        self.lbl_total_casa = ttk.Label(self, text="40""%"" Casa:", font=("Arial", 15))
        self.lbl_total_casa.pack()
        self.lbl_total_casa_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_total_casa_res.pack()

        # TOTAL - AHORRO
        self.lbl_total_ahorro = ttk.Label(self, text="10""%"" Ahorro:", font=("Arial", 15))
        self.lbl_total_ahorro.pack()
        self.lbl_total_ahorro_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_total_ahorro_res.pack()

        # TOTAL - COCHE
        self.lbl_total_coche = ttk.Label(self, text="10""%"" Coche:", font=("Arial", 15))
        self.lbl_total_coche.pack()
        self.lbl_total_coche_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_total_coche_res.pack()

        # TOTAL - CAPRICHOS
        self.lbl_total_caprichos = ttk.Label(self, text="10""%"" Caprichos:", font=("Arial", 15))
        self.lbl_total_caprichos.pack()
        self.lbl_total_caprichos_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_total_caprichos_res.pack()

        # TOTAL - LIFE
        self.lbl_total_life = ttk.Label(self, text="30""%"" Life:", font=("Arial", 15))
        self.lbl_total_life.pack()
        self.lbl_total_life_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_total_life_res.pack()

        #RESUMEN INGRESOS DEL SALARI
        self.lbl_resumen_ingresos = ttk.Label(self, text="Resumen ingresos:", font=("Arial", 20))
        self.lbl_resumen_ingresos.pack()

        # SALARI - CASA
        self.lbl_ingresos_casa = ttk.Label(self, text="40""%"" Casa:", font=("Arial", 15))
        self.lbl_ingresos_casa.pack()
        self.lbl_ingresos_casa_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_ingresos_casa_res.pack()

        # SALARI - AHORRO
        self.lbl_ingresos_ahorro = ttk.Label(self, text="10""%"" Ahorro:", font=("Arial", 15))
        self.lbl_ingresos_ahorro.pack()
        self.lbl_ingresos_ahorro_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_ingresos_ahorro_res.pack()

        # SALARI - COCHE
        self.lbl_ingresos_coche = ttk.Label(self, text="10""%"" Coche:", font=("Arial", 15))
        self.lbl_ingresos_coche.pack()
        self.lbl_ingresos_coche_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_ingresos_coche_res.pack()

        # SALARI - CAPRICHOS
        self.lbl_ingresos_caprichos = ttk.Label(self, text="10""%"" Caprichos:", font=("Arial", 15))
        self.lbl_ingresos_caprichos.pack()
        self.lbl_ingresos_caprichos_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_ingresos_caprichos_res.pack()  

        # SALARI - LIFE
        self.lbl_ingresos_life = ttk.Label(self, text="30""%"" Life:", font=("Arial", 15))
        self.lbl_ingresos_life.pack()
        self.lbl_ingresos_life_res = ttk.Label(self, text="0", font=("Arial", 15))
        self.lbl_ingresos_life_res.pack()

    #########
    #FUNCIONS
    #########
    def calcular(self):
        try:
            total = float(self.ent_total.get())
            salari = float(self.ent_salario.get())
        except ValueError:
            return

        self.lbl_total_casa_res.config(text=f"{total * 0.4:.2f}")
        self.lbl_total_ahorro_res.config(text=f"{total * 0.1:.2f}")
        self.lbl_total_coche_res.config(text=f"{total * 0.1:.2f}")
        self.lbl_total_caprichos_res.config(text=f"{total * 0.1:.2f}")
        self.lbl_total_life_res.config(text=f"{total * 0.3:.2f}")

        self.lbl_ingresos_casa_res.config(text=f"{salari * 0.4:.2f}")
        self.lbl_ingresos_ahorro_res.config(text=f"{salari * 0.1:.2f}")
        self.lbl_ingresos_coche_res.config(text=f"{salari * 0.1:.2f}")
        self.lbl_ingresos_caprichos_res.config(text=f"{salari * 0.1:.2f}")
        self.lbl_ingresos_life_res.config(text=f"{salari * 0.3:.2f}")




w = tk.Tk()
app = App(w)
app.pack(fill="both", expand="True")
app.mainloop()