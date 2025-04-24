""" ESTO ES EL PRIMERO MENU DE LOS MESEROS DONDE VAN A PODER ELEGIR ENTRE QUE MESA PONER EL PEDIDO"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import subprocess  # Para ejecutar el archivo u_mesa1.py

class MeserosWindow(QMainWindow):
    def __init__(self):
        super(MeserosWindow, self).__init__()
        loadUi('u_meseros.ui', self)  # Carga el archivo .ui

        # Conectar los botones a las funciones correspondientes
        self.pushMESAM1.clicked.connect(self.open_a_mesa1)
        self.pushMESAM2.clicked.connect(self.open_a_mesa2)
        self.pushMESAM3.clicked.connect(self.open_a_mesa3)
        self.pushMESAM4.clicked.connect(self.open_a_mesa4)
        self.pushMESAM5.clicked.connect(self.open_a_mesa5)
        self.pushMESAM6.clicked.connect(self.open_a_mesa6)

    def open_a_mesa1(self):
        # Ejecutar el archivo a_mesa1.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa1.py'])

    def open_a_mesa2(self):
        # Ejecutar el archivo a_mesa2.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa2.py'])

    def open_a_mesa3(self):
        # Ejecutar el archivo a_mesa3.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa3.py'])

    def open_a_mesa4(self):
        # Ejecutar el archivo a_mesa4.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa4.py'])

    def open_a_mesa5(self):
        # Ejecutar el archivo a_mesa5.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa5.py'])

    def open_a_mesa6(self):
        # Ejecutar el archivo a_mesa6.py
        subprocess.Popen(['python', 'd:\\POO\\PROYECTOS\\Proyectoe\\Ui\\MENU DE MESAS\\a_mesa6.py'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MeserosWindow()
    window.show()
    sys.exit(app.exec_())