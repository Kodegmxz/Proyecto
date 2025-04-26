from PyQt5 import QtWidgets
from .u_editar_ui import Ui_Dialog


class Editar(QtWidgets.QDialog):
    def __init__(self, db, parent=None):
        super(Editar, self).__init__(parent)
        self.db = db  # Store the database reference
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buscarcode.clicked.connect(self.buscar_producto_por_codigo)

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
        for tabla in tablas:
            cursor = self.db.dbcursor
            query = f"SELECT codigo, precio, nombre, cantidad, ingreso, proveedor FROM {tabla} WHERE codigo = %s"
            cursor.execute(query, (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                break

        if not resultado:
            QtWidgets.QMessageBox.information(self, "Sin resultados", "No se encontró ningún producto con ese código en las tablas.")
            return

        # Mostrar los datos en el tableWidget
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(6)
        for col_idx, value in enumerate(resultado):
            self.ui.tableWidget.setItem(0, col_idx, QtWidgets.QTableWidgetItem(str(value)))

