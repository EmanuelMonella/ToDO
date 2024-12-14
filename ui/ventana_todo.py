from PySide6.QtCore import QObject, Signal
from ui.todo_grafico import Ui_Tareas

class TareasGrafico(Ui_Tareas, QObject):
    agregar = Signal(str)
    completar = Signal(int)
    eliminar = Signal(int)

    def __init__(self, ventana):
        super().__init__()
        self.setupUi(ventana)
        self.boton_agregar.clicked.connect(self.agregar_tarea)
        self.boton_completar.clicked.connect(self.completar_tarea)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        descripcion = self.ingresar_tarea_line_edit.text().strip()
        if descripcion:
            self.agregar.emit(descripcion)
            self.ingresar_tarea_line_edit.clear()

    def completar_tarea(self):
        index = self.lista.currentIndex().row()
        if index >= 0:
            self.completar.emit(index)

    def eliminar_tarea(self):
        index = self.lista.currentIndex().row()
        if index >= 0:
            self.eliminar.emit(index)

    def mostrar_tareas(self, modelo):
        self.lista.setModel(modelo)
