from datetime import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal  # Importar pyqtSignal
from .u_agregar_ui import Ui_Dialog

class AgregarProducto(QtWidgets.QDialog):
    # Definir la señal
    producto_agregado = pyqtSignal()

    def __init__(self, db):
        super(AgregarProducto, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db

        # Conectar el botón 'Agregar' con la función correspondiente
        self.ui.agregar.clicked.connect(self.agregar_producto)

    def agregar_producto(self):
        # Obtener los valores de los campos
        codigo = self.ui.linecodigo.text().strip()
        precio = self.ui.lineprecio.text().strip()
        nombre = self.ui.linenombre.text().strip()
        cantidad = self.ui.linecantidad.text().strip()
        proveedor = self.ui.lineproveedor.text().strip()
        tabla = self.ui.comboBox.currentText()

        # Validar que todos los campos estén llenos
        if not all([codigo, precio, nombre, cantidad, proveedor]):
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Mapear el texto del ComboBox a los nombres de las tablas
        tablas = {
            "Bebidas": "b_bebidas",
            "Bebidas A.": "b_bebidasA",
            "Carnes": "b_carnes",
            "Condimentos": "b_condimentos",
            "Frutas y Verduras": "b_fya",
            "Panadería": "b_panaderia",
            "Lácteos": "b_lacteos",
        }

        nombre_tabla = tablas.get(tabla)
        if not nombre_tabla:
            QMessageBox.warning(self, "Error", "No se pudo determinar la tabla de destino.")
            return

        # Obtener la fecha actual para el campo 'ingreso'
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d")

        # Ejecutar la consulta SQL para insertar los datos
        cursor = self.db.dbcursor
        query = f"""
            INSERT INTO {nombre_tabla} (codigo, precio, nombre, cantidad, proveedor, ingreso)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (codigo, precio, nombre, cantidad, proveedor, fecha_ingreso))
            self.db.db.commit()
            QMessageBox.information(self, "Éxito", "Producto agregado correctamente.")
            
            # Emitir la señal para notificar que se agregó un producto
            self.producto_agregado.emit()
            
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al agregar el producto: {e}")