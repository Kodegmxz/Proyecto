from PyQt5 import QtCore, QtWidgets
from .u_eliminar_ui import Ui_Dialog

class Eliminar(QtWidgets.QDialog):
    actualizarTablaSignal = QtCore.pyqtSignal()  # Señal personalizada para actualizar la tabla

    def __init__(self, db, parent=None):
        super(Eliminar, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = db

        # Conectar botones a sus funciones
        self.ui.buscarcode2.clicked.connect(self.buscar_producto_por_codigo)
        self.ui.eliminar.clicked.connect(self.eliminar_producto)

    def buscar_producto_por_codigo(self):
        codigo = self.ui.linecodigo4.text().strip()

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

    def eliminar_producto(self):
        # Verificar si se encontró una tabla y un producto
        if not self.tabla_encontrada:
            QtWidgets.QMessageBox.warning(self, "Error", "Primero debe buscar un producto antes de eliminarlo.")
            return

        # Obtener el código del producto
        codigo = self.ui.linecodigo4.text().strip()

        # Confirmar la eliminación
        confirmacion = QtWidgets.QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar el producto con código {codigo}?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if confirmacion == QtWidgets.QMessageBox.No:
            return

        # Ejecutar la consulta SQL para eliminar el producto
        cursor = self.db.dbcursor
        query = f"DELETE FROM {self.tabla_encontrada} WHERE codigo = %s"
        try:
            cursor.execute(query, (codigo,))
            if cursor.rowcount > 0:  # Verificar si se eliminó alguna fila
                self.db.commit()  # Confirmar los cambios en la base de datos
                QtWidgets.QMessageBox.information(self, "Éxito", f"El producto con código {codigo} ha sido eliminado.")
                self.actualizarTablaSignal.emit()  # Emitir la señal para actualizar la tabla
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No se encontró ningún producto con ese código para eliminar.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error al eliminar el producto: {e}")

        # Limpiar el tableWidget y el campo de texto
        self.ui.tableWidget.setRowCount(0)
        self.ui.linecodigo4.clear()
