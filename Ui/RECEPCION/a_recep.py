import sys
import os
from unittest import result
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
        self.cargar_mesas(db)

        self.m_1.clicked.connect(lambda: self.upd_mesa(self.m_1, db))
        self.m_2.clicked.connect(lambda: self.upd_mesa(self.m_2, db))
        self.m_3.clicked.connect(lambda: self.upd_mesa(self.m_3, db))
        self.m_4.clicked.connect(lambda: self.upd_mesa(self.m_4, db))
        self.m_5.clicked.connect(lambda: self.upd_mesa(self.m_5, db))
        self.m_6.clicked.connect(lambda: self.upd_mesa(self.m_6, db))
        self.m_7.clicked.connect(lambda: self.upd_mesa(self.m_7, db))
        self.m_8.clicked.connect(lambda: self.upd_mesa(self.m_8, db))
        self.m_9.clicked.connect(lambda: self.upd_mesa(self.m_9, db))
        self.m_10.clicked.connect(lambda: self.upd_mesa(self.m_10, db))
        self.m_11.clicked.connect(lambda: self.upd_mesa(self.m_11, db))
        self.m_12.clicked.connect(lambda: self.upd_mesa(self.m_12, db))
        self.m_13.clicked.connect(lambda: self.upd_mesa(self.m_13, db))
        self.m_14.clicked.connect(lambda: self.upd_mesa(self.m_14, db))
        self.m_15.clicked.connect(lambda: self.upd_mesa(self.m_15, db))
        self.m_16.clicked.connect(lambda: self.upd_mesa(self.m_16, db))
        self.m_17.clicked.connect(lambda: self.upd_mesa(self.m_17, db))
        self.m_18.clicked.connect(lambda: self.upd_mesa(self.m_18, db))
        self.m_19.clicked.connect(lambda: self.upd_mesa(self.m_19, db))
        self.m_20.clicked.connect(lambda: self.upd_mesa(self.m_20, db))
        self.m_21.clicked.connect(lambda: self.upd_mesa(self.m_21, db))

        self.B_resv.clicked.connect(lambda: self.cargar_mesas())
        self.B_salir.clicked.connect(self.salir)

    def upd_mesa(self, button, db):
        color=['#6cc644','#f6c40f','#bd2c00']
        color_sub=['#5eaa3b','#d6ab0d','#ad2500']
        color_sub2=['#589f37','#cca20c','#a12000']
        style = button.styleSheet()

        current_color = style.split("QPushButton {background-color:")[1].split(";")[0].strip()
        next_color = color[(color.index(current_color) + 1) % len(color)]
        next_color_sub = color_sub[(color.index(current_color) + 1) % len(color)]
        next_color_sub2 = color_sub2[(color.index(current_color) + 1) % len(color)]
        style_n = style.replace("QPushButton {background-color: "+current_color+';', "QPushButton {background-color: "+next_color+';')
        style_nsub = style_n.replace("QPushButton:hover {background-color: "+color_sub[color.index(current_color) % len(color)]+';', "QPushButton:hover {background-color: "+next_color_sub+';')
        style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: "+color_sub2[color.index(current_color) % len(color)]+';', "QPushButton:pressed {background-color: "+next_color_sub2+';')

        db.dbcursor.execute("UPDATE Users.mesas SET v1 = %s, v2 = %s, v3 = %s WHERE mesa = %s;", (next_color, next_color_sub, next_color_sub2, button.text()))
        db.commit()
        button.setStyleSheet(style_nsub2)

    def cargar_mesas(self, db):
        for n in range (1,22):
            button = getattr(self, f'm_{n}')
            db.dbcursor.execute("SELECT v1 FROM Users.mesas WHERE mesa = %s;", (button.text(),))
            result = db.dbcursor.fetchone()
            if result[0] == '#6cc644':
                c_sub='#5eaa3b'
                c_sub2 = '#589f37'
            elif result[0] == '#f6c40f':
                c_sub = '#d6ab0d'
                c_sub2 = '#cca20c'
            else:
                c_sub = '#ad2500'
                c_sub2 = '#a12000'

            style = button.styleSheet()
            style_n = style.replace("QPushButton {background-color: #6cc644;", "QPushButton {background-color: "+result[0]+';')
            style_nsub = style_n.replace("QPushButton:hover {background-color: #5eaa3b;", "QPushButton:hover {background-color: "+c_sub+';')
            style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: #589f37;", "QPushButton:pressed {background-color: "+c_sub2+';')
            button.setStyleSheet(style_nsub2)

    def resv(self):
        pass

    def salir(self):
        from Ui.Login.a_login import Login
        mainwindow = Login(self.widget, self.db)
        self.widget.addWidget(mainwindow)
        self.widget.setFixedWidth(400)
        self.widget.setFixedHeight(500)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)




def a2(db, widget):
    recep_w = Recepcion(widget, db)
    widget.addWidget(recep_w)
    widget.setFixedWidth(901)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)
