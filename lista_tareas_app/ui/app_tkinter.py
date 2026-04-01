# interfaz gráfica creada
import tkinter as tk
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.servicio = TareaServicio()

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack()

        self.btn_completar = tk.Button(root, text="Completar Tarea", command=self.completar_tarea)
        self.btn_completar.pack()

        self.btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # ATAJOS DE TECLADO
        self.root.bind("<Return>", lambda event: self.agregar_tarea())   # Enter
        self.root.bind("c", lambda event: self.completar_tarea())        # tecla C
        self.root.bind("d", lambda event: self.eliminar_tarea())         # tecla D
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())  # Delete
        self.root.bind("<Escape>", lambda event: self.root.quit())       # Escape

    def agregar_tarea(self):
        texto = self.entry.get()
        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.servicio.completar_tarea(index)
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.servicio.eliminar_tarea(index)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            estado = "✔" if tarea.completada else "✘"
            self.lista.insert(tk.END, f"{estado} {tarea.descripcion}")