import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Recepcion(QDialog):
    def __init__(self, widget, db):
        super(Recepcion, self).__init__()
        self.original_widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_recepcion.ui")
        loadUi(ui_a, self)
        self.color=['#6cc644','#f6c40f','#bd2c00']
        self.color_sub=['#5eaa3b','#d6ab0d','#ad2500']
        self.color_sub2=['#589f37','#cca20c','#a12000']

        self.Reservaciones.hide()
        self.Reservaciones_2.hide()
        self.Reservaciones_3.hide()
        self.Reservaciones_4.hide()
        self.cargar_mesas(db)

        self.m_1.clicked.connect(lambda: self.upd_mesa(1, db))
        self.m_2.clicked.connect(lambda: self.upd_mesa(2, db))
        self.m_3.clicked.connect(lambda: self.upd_mesa(3, db))
        self.m_4.clicked.connect(lambda: self.upd_mesa(4, db))
        self.m_5.clicked.connect(lambda: self.upd_mesa(5, db))
        self.m_6.clicked.connect(lambda: self.upd_mesa(6, db))
        self.m_7.clicked.connect(lambda: self.upd_mesa(7, db))
        self.m_8.clicked.connect(lambda: self.upd_mesa(8, db))
        self.m_9.clicked.connect(lambda: self.upd_mesa(9, db))
        self.m_10.clicked.connect(lambda: self.upd_mesa(10, db))
        self.m_11.clicked.connect(lambda: self.upd_mesa(11, db))
        self.m_12.clicked.connect(lambda: self.upd_mesa(12, db))
        self.m_13.clicked.connect(lambda: self.upd_mesa(13, db))
        self.m_14.clicked.connect(lambda: self.upd_mesa(14, db))
        self.m_15.clicked.connect(lambda: self.upd_mesa(15, db))
        self.m_16.clicked.connect(lambda: self.upd_mesa(16, db))
        self.m_17.clicked.connect(lambda: self.upd_mesa(17, db))
        self.m_18.clicked.connect(lambda: self.upd_mesa(18, db))
        self.m_19.clicked.connect(lambda: self.upd_mesa(19, db))
        self.m_20.clicked.connect(lambda: self.upd_mesa(20, db))
        self.m_21.clicked.connect(lambda: self.upd_mesa(21, db))

        self.b_salir_1.clicked.connect(self.salir)

    def upd_mesa(self, n, db):
        button = getattr(self, f'm_{n}')
        style = button.styleSheet()
        current_color = style.split("QPushButton {background-color:")[1].split(";")[0].strip()
        print(current_color)
        next_color = self.color[(self.color.index(current_color) + 1) % len(self.color)]
        next_color_sub = self.color_sub[(self.color.index(current_color) + 1) % len(self.color)]
        next_color_sub2 = self.color_sub2[(self.color.index(current_color) + 1) % len(self.color)]
        print(next_color)
        print(next_color_sub)
        print(next_color_sub2)
        style_n = style.replace("QPushButton {background-color: "+current_color+';', "QPushButton {background-color: "+next_color+';')
        style_nsub = style_n.replace("QPushButton:hover {background-color: "+self.color_sub[self.color.index(current_color) % len(self.color)]+';', "QPushButton:hover {background-color: "+next_color_sub+';')
        style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: "+self.color_sub2[self.color.index(current_color) % len(self.color)]+';', "QPushButton:pressed {background-color: "+next_color_sub2+';')
        db.dbcursor.execute("UPDATE Users.mesas SET v1 = %s, v2 = %s, v3 = %s WHERE mesa = %s;", (next_color, next_color_sub, next_color_sub2, button.text()))
        db.commit()

        button.setStyleSheet(style_nsub2)

    def cargar_mesas(self, db):
        db.dbcursor.execute("SELECT v1 FROM Users.mesas")
        data = db.dbcursor.fetchall()
        for n in range(len(data)):
            dat = str(data[n])
            print(dat)
            if dat == (f"('{self.color[0]}',)"):
                c = self.color[0]
                c_sub= self.color_sub2[0]
                c_sub2 = self.color[0]
            elif dat == (f"('{self.color[1]}',)"):
                c = self.color[1]
                c_sub = self.color_sub[1]
                c_sub2 = self.color_sub2[1]
            else:
                c = self.color[2]   
                c_sub = self.color_sub[2]
                c_sub2 = self.color_sub2[2]

            button = getattr(self, f'm_{n+1}')
            style = button.styleSheet()
            style_n = style.replace("QPushButton {background-color: #6cc644;", "QPushButton {background-color: "+c+';')
            style_nsub = style_n.replace("QPushButton:hover {background-color: #5eaa3b;", "QPushButton:hover {background-color: "+c_sub+';')
            style_nsub2 = style_nsub.replace("QPushButton:pressed {background-color: #589f37;", "QPushButton:pressed {background-color: "+c_sub2+';')
            button.setStyleSheet(style_nsub2)

    def salir(self):
        from Ui.Login.a_login import Login
        mainwindow = Login(self.original_widget, self.db)
        self.original_widget.addWidget(mainwindow)
        self.original_widget.setFixedWidth(400)
        self.original_widget.setFixedHeight(500)
        self.original_widget.setCurrentIndex(self.original_widget.currentIndex()+1)



def a2(db, widget):
    recep_w = Recepcion(widget, db)
    widget.addWidget(recep_w)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)
