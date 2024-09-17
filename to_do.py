from PySide6 import QtWidgets

from ventanas import VentanaToDo

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    to_do = VentanaToDo()
    to_do.show()

    app.exec()

