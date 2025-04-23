""" ESTO ES EL PRIMERO MENU DE LOS MESEROS DONDE VAN A PODER ELEGIR ENTRE QUE MESA PONER EL PEDIDO"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import subprocess  # Para ejecutar el archivo u_mesa1.py

class MeserosWindow(QMainWindow):
    def __init__(self):
        super(MeserosWindow, self).__init__()
        loadUi('u_meseros.ui', self)  # Carga el archivo .ui

        # Conectar el botón pushMESAM1 a la función open_u_mesa1
        self.pushMESAM1.clicked.connect(self.open_a_mesa1)

    def open_a_mesa1(self):
        # Ejecutar el archivo u_mesa1.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\a_mesa1.py'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MeserosWindow()
    window.show()
    sys.exit(app.exec_())