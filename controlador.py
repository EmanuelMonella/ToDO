from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QMainWindow, QMessageBox
from gestor_tareas import GestorDeTareas, ModeloTareas
from ui.ventana_todo import TareasGrafico

class Controlador:
    def __init__(self):
        self.__gestor = GestorDeTareas()
        self.__modelo = ModeloTareas(self.__gestor)
        self.__ventana = QMainWindow()
        self.__vista = TareasGrafico(self.__ventana)
        self.__vista.mostrar_tareas(self.__modelo)
        self.__vista.agregar.connect(self.agregar_tarea)
        self.__vista.completar.connect(self.completar_tarea)
        self.__vista.eliminar.connect(self.eliminar_tarea)

    def mostrar_vista(self):
        self.__ventana.show()

    def agregar_tarea(self, descripcion):
        try:
            self.__gestor.agregar_tarea(descripcion)
            self.__modelo.layoutChanged.emit()
        except ValueError as e:
            QMessageBox.warning(self.__ventana, "Error", str(e))

    def completar_tarea(self, index):
        try:
            self.__gestor.completar_tarea(index)
            self.__modelo.dataChanged.emit(QModelIndex(), QModelIndex())
        except ValueError as e:
            QMessageBox.warning(self.__ventana, "Error", str(e))

    def eliminar_tarea(self, index):
        try:
            self.__gestor.eliminar_tarea(index)
            self.__modelo.layoutChanged.emit()
        except ValueError as e:
            QMessageBox.warning(self.__ventana, "Error", str(e))
