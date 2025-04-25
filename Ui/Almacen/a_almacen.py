from PyQt5 import QtWidgets, uic, QtCore
import sys

class AlmacenApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('alamacen mamalon.ui', self)

        # Conectar el botón 'agregar' con la función correspondiente
        self.agregar.clicked.connect(self.guardar_producto)
        # Conectar el botón 'buscar' con la función correspondiente
        self.botonbuscar.clicked.connect(self.buscar_producto)
        # Conectar el botón 'reset' con la función correspondiente
        self.botonreset.clicked.connect(self.resetear_tabla)

    def guardar_producto(self):
        # Obtener los valores de los campos de entrada
        nombre = self.linenombre.text()
        tipo = self.comboBox.currentText()
        cantidad = self.linecantidad.text()
        codigo = self.linecodigo.text()
        proveedor = self.lineproveedor.text()
        precio_unitario = self.lineprecio.text()
        fecha = QtCore.QDate.currentDate().toString("dd/MM/yyyy")

        # Validar que los campos no estén vacíos
        if not all([nombre, tipo, cantidad, codigo, proveedor, precio_unitario]):
            return

        # Obtener las pestañas del TabWidget
        tab_widget = self.tabWidget
        tab_names = [tab_widget.tabText(i).lower() for i in range(tab_widget.count())]

        # Verificar si el tipo coincide con alguna pestaña
        if tipo.lower() in tab_names:
            tab_index = tab_names.index(tipo.lower())
            tab = tab_widget.widget(tab_index)

            # Buscar la tabla dentro de la pestaña
            table = tab.findChild(QtWidgets.QTableWidget)
            if table:
                # Agregar una nueva fila a la tabla
                row_position = table.rowCount()
                table.insertRow(row_position)
                table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(codigo))
                table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(precio_unitario))
                table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(nombre))
                table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(cantidad))
                table.setItem(row_position, 4, QtWidgets.QTableWidgetItem(fecha))
                table.setItem(row_position, 5, QtWidgets.QTableWidgetItem(proveedor))

        # Limpiar los campos de entrada
        self.linenombre.clear()
        self.comboBox.setCurrentIndex(0)  # Reiniciar el combo box después de guardar
        self.linecantidad.clear()
        self.linecodigo.clear()
        self.lineproveedor.clear()
        self.lineprecio.clear()

    def buscar_producto(self):
        # Obtener el texto de búsqueda
        texto_busqueda = self.barrabusqueda.text().strip().lower()

        # Validar que el texto de búsqueda no esté vacío
        if not texto_busqueda:
            return

        # Obtener la pestaña activa
        tab_widget = self.tabWidget
        tab_index = tab_widget.currentIndex()
        tab = tab_widget.widget(tab_index)

        # Buscar la tabla dentro de la pestaña activa
        table = tab.findChild(QtWidgets.QTableWidget)
        if table:
            # Iterar sobre las filas de la tabla
            for row in range(table.rowCount()):
                match = False
                for column in range(table.columnCount()):  # Revisar todas las columnas
                    item = table.item(row, column)
                    if item and texto_busqueda in item.text().strip().lower():
                        match = True
                        break

                # Mostrar u ocultar la fila según el resultado de la búsqueda
                table.setRowHidden(row, not match)

    def resetear_tabla(self):
        # Obtener la pestaña activa
        tab_widget = self.tabWidget
        tab_index = tab_widget.currentIndex()
        tab = tab_widget.widget(tab_index)

        # Buscar la tabla dentro de la pestaña activa
        table = tab.findChild(QtWidgets.QTableWidget)
        if table:
            # Mostrar todas las filas de la tabla
            for row in range(table.rowCount()):
                table.setRowHidden(row, False)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AlmacenApp()
    window.show()
    sys.exit(app.exec_())