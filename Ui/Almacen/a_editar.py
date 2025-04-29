from PyQt5 import QtCore, QtWidgets
from .u_editar_ui import Ui_Dialog


class Editar(QtWidgets.QDialog):
    actualizarTablaSignal = QtCore.pyqtSignal()  # Señal personalizada para actualizar la tabla

    def __init__(self, db, parent=None):
        super(Editar, self).__init__(parent)
        self.db = db  # Guardar la referencia a la base de datos
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar botones a sus funciones
        self.ui.buscarcode.clicked.connect(self.buscar_producto_por_codigo)
        self.ui.actualizar.clicked.connect(self.actualizar_producto)  # Conexión del botón "Actualizar"

    def buscar_producto_por_codigo(self):
        codigo = self.ui.linecodigo.text().strip()

        if not codigo:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese un código antes de buscar.")
            return

        # Ejecutar consulta SQL para buscar el producto por código en todas las tablas
        tablas = [
            "b_bebidas",
            "b_bebidasA",
            "b_carnes",
            "b_condimentos",
            "b_fya",
            "b_lacteos",
            "b_panaderia"
        ]

        resultado = None
        self.tabla_encontrada = None  # Variable para guardar la tabla donde se encuentra el producto
        for tabla in tablas:
            cursor = self.db.dbcursor
            query = f"SELECT codigo, precio, nombre, cantidad, ingreso, proveedor FROM {tabla} WHERE codigo = %s"
            cursor.execute(query, (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                self.tabla_encontrada = tabla  # Guardar la tabla encontrada
                break

        if not resultado:
            QtWidgets.QMessageBox.information(self, "Sin resultados", "No se encontró ningún producto con ese código en las tablas.")
            return

        # Mostrar los datos en el tableWidget
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(6)
        for col_idx, value in enumerate(resultado):
            self.ui.tableWidget.setItem(0, col_idx, QtWidgets.QTableWidgetItem(str(value)))

    def actualizar_producto(self):
        if not hasattr(self, 'tabla_encontrada') or not self.tabla_encontrada:
            QtWidgets.QMessageBox.warning(self, "Error", "Primero debe buscar un producto antes de actualizar.")
            return

        codigo = self.ui.linecodigo.text().strip()

        if not codigo:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese un código antes de actualizar.")
            return

        # Obtener los valores de los campos de entrada
        precio = self.ui.lineprecio_44.text().strip()
        nombre = self.ui.linenombre_44.text().strip()
        cantidad = self.ui.linecantidad_44.text().strip()
        proveedor = self.ui.lineproveedor_44.text().strip()

        if not all([precio, nombre, cantidad, proveedor]):
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, complete todos los campos antes de actualizar.")
            return

        # Validar que los valores numéricos sean correctos
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Precio debe ser un número y cantidad debe ser un entero.")
            return

        # Ejecutar consulta SQL para actualizar el producto en la tabla encontrada
        cursor = self.db.dbcursor
        query = f"UPDATE {self.tabla_encontrada} SET precio = %s, nombre = %s, cantidad = %s, proveedor = %s WHERE codigo = %s"
        try:
            cursor.execute(query, (precio, nombre, cantidad, proveedor, codigo))
            if cursor.rowcount > 0:  # Verificar si se actualizó alguna fila
                # Confirmar los cambios en la base de datos
                self.db.commit()
                QtWidgets.QMessageBox.information(self, "Éxito", "El producto se actualizó correctamente.")
                self.actualizarTablaSignal.emit()  # Emitir la señal para actualizar la tabla
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No se encontró ningún producto con ese código para actualizar.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error al actualizar el producto: {e}")