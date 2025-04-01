import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDial, QDialog, QApplication
from PyQt5.uic import loadUi

class Recepcion(QDialog):
    def __init__(self, widget,db):
        super(Recepcion, self).__init__()
        self.widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_recepcion.ui")
        loadUi(ui_a, self)
        self.salir_boton.clicked.connect(self.salidabutton)
        self.push_hola.clicked.connect(self.hola)

    def salidabutton(self):
        from Ui.a_login import Login
        mainwindow = Login(self.widget, self.db)  # Pasar el widget a Login
        self.widget.addWidget(mainwindow)
        self.widget.setFixedWidth(400)
        self.widget.setFixedHeight(500)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)


def a2(db,widget):
    recep_w = Recepcion(widget,db)  # Pasar el widget a Recepcion
    widget.addWidget(recep_w)
    widget.setFixedWidth(800)
    widget.setFixedHeight(500)
    widget.setCurrentIndex(widget.currentIndex()+1)