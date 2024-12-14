import sys
from PySide6.QtWidgets import QApplication
from controlador import Controlador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = Controlador()
    controlador.mostrar_vista()
    sys.exit(app.exec())
