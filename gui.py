import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import openpyxl

class InterfazTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("TransPerfect GUI")
        self.root.geometry("1150x650")
        self.root.resizable(width=False, height=False)
        icono = tk.PhotoImage(file="C:/Users/kenny/OneDrive/Escritorio/TP-GUI/icon.png")
        self.root.iconphoto(True, icono)


        # Div más grande
        div_principal = tk.Frame(self.root, width=1150, height=650, bg="whitesmoke")
        div_principal.pack()
        # Primer div (izquierda)
        div_izquierda = tk.Frame(div_principal, width=180, height=650, bg="#87C8FF")
        div_izquierda.pack(side=tk.LEFT)
        div_izquierda.pack_propagate(False)  # Deshabilitar ajuste automático del tamaño
        # Segundo div (arriba)
        div_arriba = tk.Frame(div_principal, width=1150, height=80, bg='#87C8FF')
        div_arriba.pack(side=tk.TOP)

        ##################################### combobox #########################################################

        # Combobox para selección única
        opciones_combobox = ["QA Evaluations", "Tardiness"]
        self.combobox = ttk.Combobox(div_izquierda, values=opciones_combobox)
        self.combobox.pack(pady=(100, 5))

        # DateEntry para seleccionar una fecha
        self.date_entry = DateEntry(div_izquierda, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.date_entry.pack(pady=10)

        # Listbox para selección múltiple
        opciones_listbox = ["Kenny", "Josué", "Aragón", "Cascante"]
        self.listbox = tk.Listbox(div_izquierda, selectmode=tk.MULTIPLE, height=len(opciones_listbox))
        for opcion in opciones_listbox:
            self.listbox.insert(tk.END, opcion)
        self.listbox.pack(pady=10)

        # Botón "Load"
        load_button = tk.Button(div_izquierda, text="Load", command=self.load_data)
        load_button.pack(pady=10)

        ########################################## DRAG AND DROP ##############################################

        # Espacio cuadrado para arrastrar y soltar
        drop_area = tk.Label(div_izquierda, text="Drag and drop here", bg="lightgray", bd=2, relief="groove", width=20, height=5)
        drop_area.pack(pady=10, padx=10)

        # Asociar eventos de arrastrar y soltar
        drop_area.bind("<Enter>", self.drag_enter)
        drop_area.bind("<Leave>", self.drag_leave)
        drop_area.bind("<B1-Motion>", self.drop)  # Usamos B1-Motion para manejar el arrastre

        ######################################## funciones ###############################################


    def load_data(self):
        # Lógica para cargar datos según las selecciones
        selected_combobox = self.combobox.get()
        selected_date = self.date_entry.get()
        selected_listbox = self.listbox.curselection()
        print("Combobox:", selected_combobox)
        print("Date Entry:", selected_date)
        print("Listbox:", [self.listbox.get(i) for i in selected_listbox])

    ##################################### funciones drag and drop    

    def drag_enter(self, event):
        # Cambiar el color de fondo cuando el cursor entra en el área de arrastrar y soltar
        event.widget.config(bg="lightblue")

    def drag_leave(self, event):
        # Restaurar el color de fondo cuando el cursor sale del área de arrastrar y soltar
        event.widget.config(bg="lightgray")

    def drop(self, event):
        # Manejar el evento de soltar
        event.widget.config(bg="lightgray")
        file_path = event.data
        print("Archivo soltado:", file_path)

        # Verificar si el archivo es un archivo xlsx
        if file_path.lower().endswith(".xlsx"):
            # Procesar el archivo xlsx
            workbook = openpyxl.load_workbook(file_path)
            sheet_names = workbook.sheetnames
            print("Hojas del archivo xlsx:", sheet_names)
            # Puedes realizar más acciones con el archivo xlsx según tus necesidades

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTkinter(root)
    root.mainloop()
