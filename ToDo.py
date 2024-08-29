from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QStandardItem, QStandardItemModel
from todo_grafico import Ui_ToDo

class VentanaToDo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_ToDo()
        self.__ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    todo = VentanaToDo()
    todo.show()

    app.exec()
