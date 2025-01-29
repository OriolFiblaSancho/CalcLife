import ttkbootstrap as bootstrap
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Crear finestra
class App(tk.Frame):
    def __init__(self, w):
        super().__init__(w)
        self.w = w
        self.w.title("CalcLife")
        self.__create_elements()

    ####################
    # CREATION OF WIDGETS
    ####################
    def __create_elements(self):
        # TITUL PRINCIPAL
        self.lbl_mainTitle = ttk.Label(self, text="CalcLIFE", font=("Arial", 30, "bold"), padding=10)
        self.lbl_mainTitle.grid(row=0, column=0, columnspan=2)

        # INPUT FRAMES START
        self.frm_input = ttk.Frame(self)
        # FRAME TOTAL ESTALVIAT
        self.lbl_total = ttk.Label(self.frm_input, text="Dinero total:", font=("Arial", 15))
        self.lbl_total.grid(row=0, column=0, padx=5, pady=5)
        self.ent_total = ttk.Entry(self.frm_input, font=("Arial", 15))
        self.ent_total.grid(row=1, column=0, padx=5, pady=5)

        # FRAME SALARI
        self.lbl_salario = ttk.Label(self.frm_input, text="Salario:", font=("Arial", 15))
        self.lbl_salario.grid(row=0, column=1, padx=5, pady=5)
        self.ent_salario = ttk.Entry(self.frm_input, font=("Arial", 15))
        self.ent_salario.grid(row=1, column=1, padx=5, pady=5)

        self.frm_input.grid(row=1, column=0, columnspan=2, pady=10) # FEM UN PACK DE LA SECCIÓ AMB MÈTODE GRID

        # BOTÓ CALCULAR
        self.btt_calcular = ttk.Button(self, text="Calcular", command=self.calcular, width=20, style="superman.TButton")
        self.btt_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        # OUTPUT FRAMES (ON ES MOSTRA LA SORTIDA DE DADES)
        self.frm_total = ttk.Frame(self, borderwidth=2, relief="solid", padding=10) # MAIN FRAME TOTAL ESTALVIAT
        
        self.lbl_resumen_total = ttk.Label(self.frm_total, text="Resumen total:", font=("Arial", 20))
        self.lbl_resumen_total.pack(anchor="center", pady=5)
        self.lbl_total_details = ttk.Label(self.frm_total,text="Introduzca el dinero total para ver el resumen",font=("Arial", 14))
        self.lbl_total_details.pack(anchor="center", pady=5)
        self.frm_total.grid(row=3, column=0, padx=10, pady=10, sticky="n")

        # FRAME PER AL SALARI
        self.frm_salario = ttk.Frame(self, borderwidth=2, relief="solid", padding=10) # MAIN FRAME SALARI
        
        self.lbl_resumen_salario = ttk.Label(self.frm_salario, text="Resumen ingresos:", font=("Arial", 20))
        self.lbl_resumen_salario.pack(anchor="center", pady=5)
        self.lbl_salario_details = ttk.Label(self.frm_salario,text="Introduzca el salario para ver el resumen",font=("Arial", 14))
        self.lbl_salario_details.pack(anchor="center", pady=5)
        self.frm_salario.grid(row=3, column=1, padx=10, pady=10, sticky="n")

        # Placeholders per als gràfics, així no es mostren
        self.canvas_total = None
        self.canvas_salario = None

    

    #########
    # FUNCIONS
    #########
    def toggle_theme(self):
        pass

    def calcular(self):
        try:
            total = self.ent_total.get()
            salario = self.ent_salario.get()

            total = float(total) if total else None
            salario = float(salario) if salario else None

            if total is None and salario is None:
                raise ValueError("Debe llenar al menos un campo")

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada no válida: {e}")
            return

        # Si total no es None (hi ha data al input) actualitzem els labels i creem la llista per a generar el graph
        if total is not None:
            total_distribution = [total * 0.4, total * 0.1, total * 0.1, total * 0.1, total * 0.3]
            # Definim el text que es mostrarà als labels de manera formatada
            details_text = f"Casa: {total_distribution[0]:.2f}\nAhorro: {total_distribution[1]:.2f}\n" \
                           f"Coche: {total_distribution[2]:.2f}\nCaprichos: {total_distribution[3]:.2f}\n" \
                           f"Life: {total_distribution[4]:.2f}"
            self.lbl_total_details.config(text=details_text)
            self.show_pie_chart(total_distribution, "Dinero Total", "Casa\nAhorro\nCoche\nCaprichos\nLife", self.frm_total, "canvas_total")
        else: # Esborrem instàncies prèvies del gràfic
            self.clear_pie_chart(self.canvas_total)
            self.lbl_total_details.config(text="Introduzca el dinero total para ver el resumen")

        # Igual que el bloc de dalt
        if salario is not None:
            salario_distribution = [salario * 0.4, salario * 0.1, salario * 0.1, salario * 0.1, salario * 0.3]
            details_text = f"Casa: {salario_distribution[0]:.2f}\nAhorro: {salario_distribution[1]:.2f}\n" \
                           f"Coche: {salario_distribution[2]:.2f}\nCaprichos: {salario_distribution[3]:.2f}\n" \
                           f"Life: {salario_distribution[4]:.2f}"
            self.lbl_salario_details.config(text=details_text)
            self.show_pie_chart(salario_distribution, "Salario", "Casa\nAhorro\nCoche\nCaprichos\nLife", self.frm_salario, "canvas_salario")
        else:
            self.clear_pie_chart(self.canvas_salario)
            self.lbl_salario_details.config(text="Introduzca el salario para ver el resumen")

        # Fem un resize dinàmic de la finestra
        self.w.update_idletasks()
        self.w.geometry("")  # Al no passar paràmetres, s'adapta a la mida del contingut

    def show_pie_chart(self, data, title, labels, frame, canvas_attr):
        # Creem la figura i els axis (X,Y) amb mathplotlib
        # fig = Figure object que conté el graph. | ax = Axis object on es dibuixa el graph. | figsize = Mida del graph en inches
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(data, labels=labels.split("\n"), autopct="%1.1f%%", startangle=90) # Extraem les dades separant-les amb salts de línia donant una llista. 
        ax.set_title(title)

        # Incrustem el graph a tkinter (si ja existeix s'elimina)
        if getattr(self, canvas_attr):
            getattr(self, canvas_attr).get_tk_widget().destroy()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(pady=10)
        setattr(self, canvas_attr, canvas) # Actualitzem els placeholders pel graph real

    # Eliminem instàncies del graph si estaven creades
    def clear_pie_chart(self, canvas):
        if canvas:
            canvas.get_tk_widget().destroy()



w = tk.Tk()
w.geometry("815x420")
w.resizable(False, False)
style = bootstrap.Style(theme="darkly")
w = style.master
app = App(w)
app.pack(fill="both", expand=True)
app.mainloop()
