import tkinter as tk
from modelos.tarea import Tarea
from servicios.tarea_servicio import TareaServicio

class App:
    def __init__(self):
        self.servicio = TareaServicio()

        self.root = tk.Tk()
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Entrada
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        # Botones
        tk.Button(self.root, text="Agregar", command=self.agregar_tarea).pack()
        tk.Button(self.root, text="Completar", command=self.completar_tarea).pack()
        tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea).pack()

        # Lista
        self.lista = tk.Listbox(self.root)
        self.lista.pack(fill=tk.BOTH, expand=True, pady=10)

        # 🔥 ATAJOS DE TECLADO
        self.root.bind("<Return>", lambda event: self.agregar_tarea())
        self.root.bind("c", lambda event: self.completar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def agregar_tarea(self):
        texto = self.entry.get()

        if texto == "":
            return

        tarea = Tarea(texto)
        self.servicio.agregar_tarea(tarea)

        self.actualizar_lista()
        self.entry.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        self.servicio.completar_tarea(index)

        self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        self.servicio.eliminar_tarea(index)

        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for i, tarea in enumerate(self.servicio.listar_tareas()):
            texto = tarea.descripcion

            if tarea.completada:
                texto = "✔ " + texto
                self.lista.insert(tk.END, texto)
                self.lista.itemconfig(i, fg="green")
            else:
                texto = "❌ " + texto
                self.lista.insert(tk.END, texto)
                self.lista.itemconfig(i, fg="black")

    def run(self):
        self.root.mainloop()