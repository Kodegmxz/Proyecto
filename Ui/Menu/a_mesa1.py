"""AQUI SERA DONDE LOS MESEROS ESCOJAN LOS PRODUCTOS QUE DESEAN LOS DE CADA MESA Y AHI MISMO SE HARA LA SUMA TOTAL DE CADA COSA"""

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox

class MesaDialog(QDialog):
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        uic.loadUi("d:/POO/PROYECTOS/Proyectoe/Ui/u_mesa1.ui", self)

        # Conectar los botones a sus funciones
        self.arroz1.clicked.connect(lambda: self.agregar_producto("Arroz", 1, 10.0))
        self.pera1.clicked.connect(lambda: self.agregar_producto("Pera", 1, 5.0))
        self.hamburguesa1.clicked.connect(lambda: self.agregar_producto("Hamburguesa", 1, 15.0))
        self.pizza1.clicked.connect(lambda: self.agregar_producto("Pizza", 1, 20.0))


        self.cuenta1.cellChanged.connect(self.actualizar_total)

        # Conectar el botón de borrar
        self.borrar.clicked.connect(self.borrar_fila)

        # total
        self.total = 0.0

    def agregar_producto(self, producto, cantidad, precio):
        # Agregar producto a la tabla
        row_position = self.cuenta1.rowCount()
        self.cuenta1.insertRow(row_position)
        self.cuenta1.setItem(row_position, 0, QTableWidgetItem(producto))
        self.cuenta1.setItem(row_position, 1, QTableWidgetItem(str(cantidad)))
        self.cuenta1.setItem(row_position, 2, QTableWidgetItem(f"{precio:.2f}"))

        # Actualizar el total
        self.actualizar_total()

    def actualizar_total(self):
        # Recalcular el total sumando los valores de la columna de precios
        self.total = 0.0
        for row in range(self.cuenta1.rowCount()):
            try:
                cantidad = int(self.cuenta1.item(row, 1).text())
                precio = float(self.cuenta1.item(row, 2).text())
                self.total += cantidad * precio
            except (ValueError, AttributeError):
                # Ignorar filas con datos inválidos o incompletos
                continue

        # Actualizar el QLabel con el nuevo total
        self.total1.setText(f"TOTAL: {self.total:.2f}")

    def borrar_fila(self):
        # Obtener la fila seleccionada
        selected_row = self.cuenta1.currentRow()
        if selected_row == -1:
            # Mostrar un mensaje si no hay ninguna fila seleccionada
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una fila para borrar.")
            return

        # Confirmar la eliminación
        confirm = QMessageBox.question(self, "Confirmar", "¿Estás seguro de que deseas borrar esta fila?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # Eliminar la fila seleccionada
            self.cuenta1.removeRow(selected_row)
            # Actualizar el total después de borrar
            self.actualizar_total()

# Este archivo no debe ejecutarse directamente si es un subcomponente.
# Sin embargo, para pruebas, puedes usar el siguiente bloque:
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    dialog = MesaDialog()
    dialog.exec_()