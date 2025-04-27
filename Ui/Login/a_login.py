""" ESTE ES EL LOGIN PRINCIPAL DE LA APLICACION """
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDial, QDialog, QApplication
from PyQt5.uic import loadUi

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

class Login(QDialog):
    def __init__(self, widget,db):
        super(Login, self).__init__()
        self.widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_l = os.path.dirname(os.path.abspath(__file__))
        ui_l = os.path.join(dir_l, "u_login.ui")
        loadUi(ui_l, self)
        self.pushlogin.clicked.connect(self.loginbutton)


    def loginbutton(self):
        from Classes.users import usuario
        usr = usuario(self.id_emp.text(), self.pwd_emp.text())
        if self.id_emp.text() and self.pwd_emp.text():
            usr.login(self.db, self.widget) # Referencia db y widged

    def cierre(self, event):
        pass

def a1(db):
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = Login(widget,db)  # Pasar el widget y db al inicio para poder ejecutar la db en otras funciones
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(500)
    widget.show()
    sys.exit(app.exec_())