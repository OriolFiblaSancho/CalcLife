#Importar libreries
import ttkbootstrap as bs

import tkinter as tk
from tkinter import ttk

#Crear finestra
w = tk.Tk()
w.title("CalcLife")
w.geometry("400x800+600+0")

#FUNCIONS
def calcular():
    
    pass


#INPUT DE DINERS TOTALS I SALARI
lbl_title = ttk.Label(w, text="INTRODUCE LOS DATOS:", font=("Arial", 20))
lbl_title.pack()

lbl_total = ttk.Label(w, text="Dinero total:", font=("Arial", 15))
lbl_total.pack()
ent_total = ttk.Entry(w, font=("Arial", 15))
ent_total.pack()

lbl_salario = ttk.Label(w, text="Salario:", font=("Arial", 15))
lbl_salario.pack()
ent_salario = ttk.Entry(w, font=("Arial", 15))
ent_salario.pack()

btt_calcular = ttk.Button(w, text="Calcular", command=lambda:calcular(), width=20)
btt_calcular.pack()

#RESUMEN TOTAL DE DINERS
lbl_resumen_total = ttk.Label(w, text="Resumen total:", font=("Arial", 20))
lbl_resumen_total.pack()

# TOTAL - CASA
lbl_total_casa = ttk.Label(w, text="40""%""casa:", font=("Arial", 15))
lbl_total_casa.pack()
lbl_total_casa_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_total_casa_res.pack()

# TOTAL - AHORRO
lbl_total_ahorro = ttk.Label(w, text="10""%""ahorro:", font=("Arial", 15))
lbl_total_ahorro.pack()
lbl_total_ahorro_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_total_ahorro_res.pack()

# TOTAL - COCHE
lbl_total_coche = ttk.Label(w, text="10""%""coche:", font=("Arial", 15))
lbl_total_coche.pack()
lbl_total_coche_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_total_coche_res.pack()

# TOTAL - CAPRICHOS
lbl_total_caprichos = ttk.Label(w, text="10""%""caprichos:", font=("Arial", 15))
lbl_total_caprichos.pack()
lbl_total_caprichos_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_total_caprichos_res.pack()

# TOTAL - LIFE
lbl_total_life = ttk.Label(w, text="30""%""life:", font=("Arial", 15))
lbl_total_life.pack()
lbl_total_life_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_total_life_res.pack()

#RESUMEN INGRESOS DEL SALARI
lbl_resumen_ingresos = ttk.Label(w, text="Resumen ingresos:", font=("Arial", 20))
lbl_resumen_ingresos.pack()

# SALARI - CASA
lbl_ingresos_casa = ttk.Label(w, text="40""%""casa:", font=("Arial", 15))
lbl_ingresos_casa.pack()
lbl_ingresos_casa_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_ingresos_casa_res.pack()

# SALARI - AHORRO
lbl_ingresos_ahorro = ttk.Label(w, text="10""%""ahorro:", font=("Arial", 15))
lbl_ingresos_ahorro.pack()
lbl_ingresos_ahorro_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_ingresos_ahorro_res.pack()

# SALARI - COCHE
lbl_ingresos_coche = ttk.Label(w, text="10""%""coche:", font=("Arial", 15))
lbl_ingresos_coche.pack()
lbl_ingresos_coche_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_ingresos_coche_res.pack()

# SALARI - CAPRICHOS
lbl_ingresos_caprichos = ttk.Label(w, text="10""%""caprichos:", font=("Arial", 15))
lbl_ingresos_caprichos.pack()
lbl_ingresos_caprichos_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_ingresos_caprichos_res.pack()  

# SALARI - LIFE
lbl_ingresos_life = ttk.Label(w, text="30""%""life:", font=("Arial", 15))
lbl_ingresos_life.pack()
lbl_ingresos_life_res = ttk.Label(w, text="0", font=("Arial", 15))
lbl_ingresos_life_res.pack()


w.mainloop()