import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.id_emp = None
        self.pwd_emp = None

        dir = os.path.dirname(os.path.abspath(__file__))#Busca y carga el archivo
        ui = os.path.join(dir, "login.ui")
        loadUi(ui, self)
        
        self.id_emp = self.findChild(QtWidgets.QLineEdit, "id_emp") # Asigna los datos del formulario a la classe
        self.pwd_emp = self.findChild(QtWidgets.QLineEdit, "pwd_emp")
        
        self.pushlogin.clicked.connect(self.loginbutton)

    def loginbutton(self):
        id_text = self.id_emp.text()
        pwd_text = self.pwd_emp.text()
        
        # Almacena los valores en atributos de la instancia
        self.stored_id = id_text
        self.stored_pwd = pwd_text

def a1():
    app = QApplication(sys.argv)
    mainwindow = Login()
    mainwindow.show()
    app.exec_()
    return mainwindow.stored_id, mainwindow.stored_pwd #17/03/25 Aqui debemos cerrar la app para acceder al return