class TareaServicio:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        return self.tareas

    def completar_tarea(self, index):
        self.tareas[index].completada = True

    def eliminar_tarea(self, index):
        self.tareas.pop(index)