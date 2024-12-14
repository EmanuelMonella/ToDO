from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtGui import QFont

class Tarea:
    def __init__(self, descripcion):
        if not descripcion.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía")
        self.__descripcion = descripcion
        self.__estado = 'pendiente'

    def completar(self):
        self.__estado = 'completada'

    def es_completada(self):
        return self.__estado == 'completada'

    def mostrar(self):
        return self.__descripcion

class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)

    def completar_tarea(self, index):
        try:
            tarea = self.__tareas[index]
            if tarea.es_completada():
                raise ValueError("La tarea ya está completada")
            tarea.completar()
        except IndexError:
            raise ValueError("Ninguna tarea para completar")

    def eliminar_tarea(self, index):
        try:
            del self.__tareas[index]
        except IndexError:
            raise ValueError("Ninguna tarea para eliminar")

    def obtener_tareas(self):
        return self.__tareas

    def contar_tareas(self):
        return len(self.__tareas)

class ModeloTareas(QAbstractListModel):
    def __init__(self, gestor: GestorDeTareas):
        super().__init__()
        self.__gestor = gestor

    def rowCount(self, parent=QModelIndex()):
        return self.__gestor.contar_tareas()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= self.rowCount():
            return None
        tarea = self.__gestor.obtener_tareas()[index.row()]
        if role == Qt.DisplayRole:
            return tarea.mostrar()
        elif role == Qt.FontRole and tarea.es_completada():
            font = QFont()
            font.setStrikeOut(True)
            return font

        return None
