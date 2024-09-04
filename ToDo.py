from PySide6 import QtWidgets

from recursos.ventanas import VentanaToDo

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    todo = VentanaToDo()
    todo.show()

    app.exec()

