import sys
import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

# Ruta del archivo para guardar el estado de los botones
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estado_botones.json')

class Recepcion(QDialog):
    def __init__(self, widget, db):
        super(Recepcion, self).__init__()
        self.widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_recepcion.ui")
        loadUi(ui_a, self)
        
        # Conectar los botones de las mesas a la misma función
        self.pushMESA1.clicked.connect(lambda: self.cambiar_color(self.pushMESA1))
        self.pushMESA2.clicked.connect(lambda: self.cambiar_color(self.pushMESA2))
        self.pushMESA3.clicked.connect(lambda: self.cambiar_color(self.pushMESA3))
        self.pushMESA4.clicked.connect(lambda: self.cambiar_color(self.pushMESA4))
        self.pushMESA5.clicked.connect(lambda: self.cambiar_color(self.pushMESA5))
        self.pushMESA6.clicked.connect(lambda: self.cambiar_color(self.pushMESA6))
        
        # Conectar el botón de "salir" para cambiar de ventana
        self.salir_boton.clicked.connect(self.salidabutton)
        
        self.pushsave.clicked.connect(self.guardar_estado)

        self.cargar_estado()

    def salidabutton(self):
        from Ui.a_login import Login
        mainwindow = Login(self.widget, self.db)
        self.widget.addWidget(mainwindow)
        self.widget.setFixedWidth(400)
        self.widget.setFixedHeight(500)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def cambiar_color(self, boton):
        colores = ['rgb(0, 255, 0)', 'rgb(255, 0, 0)', 'rgb(255, 255, 0)']
        
        # Obtener el color actual del botón
        style = boton.styleSheet()
        if "background-color" in style:
            # Extraer el valor de background-color
            current_color = style.split("background-color:")[1].split(";")[0].strip()
        else:
            current_color = 'rgb(0, 255, 0)'
        
        #Calcular el siguiente color
        next_color = colores[(colores.index(current_color) + 1) % len(colores)]
        boton.setStyleSheet(f'background-color: {next_color};')

    def guardar_estado(self):
        #Guarda el color actual de cada botón
        estados = {
            "mesa1": self.pushMESA1.styleSheet(),
            "mesa2": self.pushMESA2.styleSheet(),
            "mesa3": self.pushMESA3.styleSheet(),
            "mesa4": self.pushMESA4.styleSheet(),
            "mesa5": self.pushMESA5.styleSheet(),
            "mesa6": self.pushMESA6.styleSheet(),
        }
        try:
            with open(STATE_FILE, 'w') as f:
                json.dump(estados, f)
            print("Estado de botones guardado correctamente.")
        except Exception as e:
            print("Error al guardar el estado:", e)

    def cargar_estado(self):
        #Carga el color de cada botón desde el archivo JSON, si existe.
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, 'r') as f:
                    estados = json.load(f)
                self.pushMESA1.setStyleSheet(estados.get("mesa1", ""))
                self.pushMESA2.setStyleSheet(estados.get("mesa2", ""))
                self.pushMESA3.setStyleSheet(estados.get("mesa3", ""))
                self.pushMESA4.setStyleSheet(estados.get("mesa4", ""))
                self.pushMESA5.setStyleSheet(estados.get("mesa5", ""))
                self.pushMESA6.setStyleSheet(estados.get("mesa6", ""))
                print("Estado de botones cargado correctamente.")
            except Exception as e:
                print("Error al cargar el estado:", e)

def a2(db, widget):
    recep_w = Recepcion(widget, db)
    widget.addWidget(recep_w)
    widget.setFixedWidth(800)
    widget.setFixedHeight(500)
    widget.setCurrentIndex(widget.currentIndex() + 1)
