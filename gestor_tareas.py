from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt
from PySide6.QtGui import QFont

class Tarea:
    def __init__(self, descripcion):
        if not descripcion.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía")
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

class GestorDeTareas(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.tareas = []

    def agregar_tarea(self, descripcion):
        if not descripcion.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía")
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.tareas.append(Tarea(descripcion))
        self.endInsertRows()

    def completar_tarea(self, index):
        if index < 0 or index >= len(self.tareas):
            raise ValueError("Índice fuera de rango")
        tarea = self.tareas[index]
        if tarea.completada:
            raise ValueError("La tarea ya está completada")
        tarea.completar()
        self.dataChanged.emit(self.index(index), self.index(index), [Qt.DisplayRole, Qt.FontRole])

    def eliminar_tarea(self, index):
        if index < 0 or index >= len(self.tareas):
            raise ValueError("Índice fuera de rango")
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.tareas[index]
        self.endRemoveRows()

    def rowCount(self, parent=QModelIndex()):
        return len(self.tareas)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= self.rowCount():
            return None
        tarea = self.tareas[index.row()]
        if role == Qt.DisplayRole:
            return tarea.descripcion
        if role == Qt.FontRole and tarea.completada:
            font = QFont()
            font.setStrikeOut(True)
            return font
        return None
