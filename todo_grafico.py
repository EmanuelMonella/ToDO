# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_grafico.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QWidget)
import recursos.logo_rc

class Ui_ToDo(object):
    def setupUi(self, ToDo):
        if not ToDo.objectName():
            ToDo.setObjectName(u"ToDo")
        ToDo.resize(341, 286)
        ToDo.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.gridLayout = QGridLayout(ToDo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 2, 1, 1)

        self.nueva_tarea = QLineEdit(ToDo)
        self.nueva_tarea.setObjectName(u"nueva_tarea")
        self.nueva_tarea.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"")

        self.gridLayout.addWidget(self.nueva_tarea, 0, 0, 1, 4)

        self.agregar_tarea = QPushButton(ToDo)
        self.agregar_tarea.setObjectName(u"agregar_tarea")
        self.agregar_tarea.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.gridLayout.addWidget(self.agregar_tarea, 0, 4, 1, 1)

        self.eliminar_tarea = QPushButton(ToDo)
        self.eliminar_tarea.setObjectName(u"eliminar_tarea")
        self.eliminar_tarea.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.gridLayout.addWidget(self.eliminar_tarea, 4, 4, 1, 1)

        self.tableView = QTableView(ToDo)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout.addWidget(self.tableView, 1, 0, 2, 5)

        self.logo = QLabel(ToDo)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setPixmap(QPixmap(u":/prefijoNuevo/To_Do.png"))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 4, 1, 1, 1)


        self.retranslateUi(ToDo)
        self.agregar_tarea.clicked.connect(ToDo._VentanaToDo__agregar_tarea)
        self.eliminar_tarea.clicked.connect(ToDo._VentanaToDo__eliminar_tarea)

        QMetaObject.connectSlotsByName(ToDo)
    # setupUi

    def retranslateUi(self, ToDo):
        ToDo.setWindowTitle(QCoreApplication.translate("ToDo", u"ToDo Loco", None))
        self.nueva_tarea.setPlaceholderText(QCoreApplication.translate("ToDo", u"Ingrese una nueva tarea", None))
        self.agregar_tarea.setText(QCoreApplication.translate("ToDo", u"Agregar tarea", None))
        self.eliminar_tarea.setText(QCoreApplication.translate("ToDo", u"Eliminar tarea", None))
        self.logo.setText("")
    # retranslateUi

