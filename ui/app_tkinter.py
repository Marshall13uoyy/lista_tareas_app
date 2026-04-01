import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas Pro")
        self.root.geometry("500x400")

        self.servicio = TareaServicio()

        # ===== INPUT =====
        frame_top = tk.Frame(root)
        frame_top.pack(pady=10)

        self.entry = tk.Entry(frame_top, width=35)
        self.entry.pack(side=tk.LEFT, padx=5)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        tk.Button(
            frame_top, 
            text="Añadir", 
            command=self.agregar_tarea, 
            bg="#4CAF50", 
            fg="white"
        ).pack(side=tk.LEFT)

        # ===== TABLA =====
        self.tree = ttk.Treeview(root, columns=("ID", "Tarea"), show="headings", height=12)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tarea", text="Descripción")
        self.tree.column("ID", width=50)
        self.tree.column("Tarea", width=350)
        self.tree.pack(pady=10)

        # Estilo completado
        self.tree.tag_configure("completado", foreground="gray")

        # Evento doble clic
        self.tree.bind("<Double-1>", self.completar_tarea_evento)

        # ===== BOTONES =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones, 
            text="Completar", 
            command=self.completar_tarea, 
            bg="#2196F3", 
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_botones, 
            text="Eliminar", 
            command=self.eliminar_tarea, 
            bg="#f44336", 
            fg="white"
        ).pack(side=tk.LEFT, padx=5)

    # ===== FUNCIONES =====
    def refrescar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            tag = ""

            if tarea.completado:
                texto = "✔ " + texto
                tag = "completado"

            self.tree.insert("", tk.END, values=(tarea.id, texto), tags=(tag,))

    def agregar_tarea(self):
        descripcion = self.entry.get().strip()

        if descripcion:
            self.servicio.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.refrescar_lista()

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def obtener_id_seleccionado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            return None

        item = self.tree.item(seleccion)
        return int(item["values"][0])

    def completar_tarea(self):
        id_tarea = self.obtener_id_seleccionado()

        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.refrescar_lista()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        id_tarea = self.obtener_id_seleccionado()

        if id_tarea:
            self.servicio.eliminar_tarea(id_tarea)
            self.refrescar_lista()