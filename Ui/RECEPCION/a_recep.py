import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Recepcion(QDialog):
    def __init__(self, widget, db):
        super(Recepcion, self).__init__()
        self.widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_recepcion.ui")
        loadUi(ui_a, self)

        self.m_1.clicked.connect(self.mesa)
        self.m_2.clicked.connect(self.mesa)
        self.m_3.clicked.connect(self.mesa)
        self.m_4.clicked.connect(self.mesa)
        self.m_5.clicked.connect(self.mesa)
        self.m_6.clicked.connect(self.mesa)
        self.m_7.clicked.connect(self.mesa)
        self.m_8.clicked.connect(self.mesa)
        self.m_9.clicked.connect(self.mesa)
        self.m_10.clicked.connect(self.mesa)
        self.m_11.clicked.connect(self.mesa)
        self.m_12.clicked.connect(self.mesa)
        self.m_13.clicked.connect(self.mesa)
        self.m_14.clicked.connect(self.mesa)
        self.m_15.clicked.connect(self.mesa)
        self.m_16.clicked.connect(self.mesa)
        self.m_17.clicked.connect(self.mesa)
        self.m_18.clicked.connect(self.mesa)
        self.m_19.clicked.connect(self.mesa)
        self.m_20.clicked.connect(self.mesa)
        self.m_21.clicked.connect(self.mesa)





def a2(db, widget):
    recep_w = Recepcion(widget, db)
    widget.addWidget(recep_w)
    widget.setFixedWidth(901)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)
