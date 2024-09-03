from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QStandardItem, QStandardItemModel
from recursos.todo_grafico import Ui_ToDo

class VentanaToDo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_ToDo()
        self.__ui.setupUi(self)

        self.modelo = QStandardItemModel()
        self.modelo.setHorizontalHeaderLabels(['Completada', 'Tarea'])
        self.__ui.tableView.setModel(self.modelo)

    def __agregar_tarea(self):
        tarea_nueva = self.__ui.nueva_tarea.text()
        if tarea_nueva:
            checkbox_item = QStandardItem()
            checkbox_item.setCheckable(True)
            checkbox_item.setCheckState(QtCore.Qt.Unchecked)

            tarea_item = QStandardItem(tarea_nueva)

            self.modelo.appendRow([checkbox_item, tarea_item])
            self.__ui.nueva_tarea.clear()


    def __eliminar_tarea(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    todo = VentanaToDo()
    todo.show()

    app.exec()

