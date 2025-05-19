import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication , QMessageBox
from PyQt5.uic import loadUi
from datetime import datetime
from PyQt5.QtCore import pyqtSignal  # Agrega esta línea


class Almacen(QtWidgets.QWidget):
    producto_agregado = pyqtSignal()  # Agrega esta línea

    def __init__(self, widget, db):
        super(Almacen, self).__init__()
        self.widget = widget
        self.db = db
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_almacen.ui")
        loadUi(ui_a, self)

        # Conectar botones a sus funciones
        self.botonbuscar.clicked.connect(self.buscar_producto)
        self.botonreset.clicked.connect(self.resetear_tabla)
        self.buscareditar.clicked.connect(self.buscar_producto_por_codigo)
        self.actualizar.clicked.connect(self.actualizar_producto)
        self.buscareliminar.clicked.connect(self.buscarcodeeliminar)
        self.eliminar.clicked.connect(self.eliminar_producto)
        self.agregar.clicked.connect(self.agregar_producto)



        self.cargar_datos_iniciales()
        self.wagregar.hide()
        self.weditar.hide()
        self.weliminar.hide()


    def cargar_datos_iniciales(self):
        self.cargar_bebidas()
        self.cargar_bebidasA()
        self.cargar_carnes()
        self.cargar_condimentos()
        self.cargar_fya()
        self.cargar_lacteos()
        self.cargar_panaderia()

    def cargar_bebidas(self):
        self.cargar_datos_tabla_personalizada(0, "b_bebidas")

    def cargar_bebidasA(self):
        self.cargar_datos_tabla_personalizada(1, "b_bebidasA")

    def cargar_carnes(self):
        self.cargar_datos_tabla_personalizada(2, "b_carnes")

    def cargar_condimentos(self):
        self.cargar_datos_tabla_personalizada(3, "b_condimentos")

    def cargar_fya(self):
        self.cargar_datos_tabla_personalizada(4, "b_fya")

    def cargar_lacteos(self):
        self.cargar_datos_tabla_personalizada(5, "b_lacteos")

    def cargar_panaderia(self):
        self.cargar_datos_tabla_personalizada(6, "b_panaderia")

    def cargar_datos_tabla_personalizada(self, tab_index, nombre_tabla):
        # Obtener la pestaña correspondiente
        tab = self.tabWidget.widget(tab_index)
        table = tab.findChild(QtWidgets.QTableWidget)

        if table:
            # Ejecutar consulta SQL para obtener los datos
            cursor = self.db.dbcursor
            query = f"SELECT codigo, precio, nombre, cantidad, ingreso, proveedor FROM {nombre_tabla}"
            cursor.execute(query)
            resultados = cursor.fetchall()

            # Configurar la tabla
            table.setRowCount(len(resultados))
            table.setColumnCount(6)  # Asumimos 6 columnas

            # Insertar los datos en la tabla
            for row_idx, row_data in enumerate(resultados):
                for col_idx, value in enumerate(row_data):
                    table.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))

    def buscar_producto(self):
        # Obtener el texto de búsqueda
        texto_busqueda = self.barrabusqueda.text().strip().lower()

        # Validar que el texto de búsqueda no esté vacío
        if not texto_busqueda:
            QtWidgets.QMessageBox.warning(self, "Búsqueda vacía", "Por favor, ingrese un texto para buscar.")
            return

        # Obtener la pestaña activa
        tab_widget = self.tabWidget
        tab_index = tab_widget.currentIndex()
        tab = tab_widget.widget(tab_index)

        # Diccionario que asocia pestañas con nombres de tablas en la base de datos
        tablas = {
            0: "b_bebidas",
            1: "b_bebidasA",
            2: "b_carnes",
            3: "b_condimentos",
            4: "b_fya",
            5: "b_lacteos",
            6: "b_panaderia"
        }

        nombre_tabla = tablas.get(tab_index)
        if not nombre_tabla:
            QtWidgets.QMessageBox.warning(self, "Error", "No se pudo determinar la tabla activa.")
            return

        # Ejecutar consulta SQL para buscar los datos
        cursor = self.db.dbcursor
        query = f"""
            SELECT codigo, precio, nombre, cantidad, ingreso, proveedor 
            FROM {nombre_tabla} 
            WHERE LOWER(codigo) LIKE %s 
               OR LOWER(nombre) LIKE %s 
               OR LOWER(proveedor) LIKE %s
        """
        cursor.execute(query, (f"%{texto_busqueda}%", f"%{texto_busqueda}%", f"%{texto_busqueda}%"))
        resultados = cursor.fetchall()

        # Buscar la tabla dentro de la pestaña activa
        table = tab.findChild(QtWidgets.QTableWidget)
        if table:
            # Configurar la tabla con los resultados
            table.setRowCount(len(resultados))
            table.setColumnCount(6)  # Asumimos 6 columnas

            for row_idx, row_data in enumerate(resultados):
                for col_idx, value in enumerate(row_data):
                    table.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))

    def resetear_tabla(self):
        # Obtener la pestaña activa
        tab_widget = self.tabWidget
        tab_index = tab_widget.currentIndex()

        # Diccionario que asocia pestañas con nombres de tablas en la base de datos
        tablas = {
            0: "b_bebidas",
            1: "b_bebidasA",
            2: "b_carnes",
            3: "b_condimentos",
            4: "b_fya",
            5: "b_lacteos",
            6: "b_panaderia"
        }

        nombre_tabla = tablas.get(tab_index)
        if not nombre_tabla:
            QtWidgets.QMessageBox.warning(self, "Error", "No se pudo determinar la tabla activa.")
            return

        # Recargar los datos de la tabla activa
        self.cargar_datos_tabla_personalizada(tab_index, nombre_tabla)


    def agregar_producto(self):
        # Obtener los valores de los campos
        codigo = self.linecodigo.text().strip()
        precio = self.lineprecio.text().strip()
        nombre = self.linenombre.text().strip()
        cantidad = self.linecantidad.text().strip()
        proveedor = self.lineproveedor.text().strip()
        tabla = self.comboBox.currentText()

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

            # self.close()  # <-- Quita o comenta esta línea
            # Opcional: limpia los campos para permitir agregar otro producto
            self.linecodigo.clear()
            self.lineprecio.clear()
            self.linenombre.clear()
            self.linecantidad.clear()
            self.lineproveedor.clear()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al agregar el producto: {e}")


    def buscar_producto_por_codigo(self):
        codigo = self.codigoeditar.text().strip()

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
        self.tableeditar.setRowCount(1)
        self.tableeditar.setColumnCount(6)
        for col_idx, value in enumerate(resultado):
            self.tableeditar.setItem(0, col_idx, QtWidgets.QTableWidgetItem(str(value)))

    def actualizar_producto(self):
        if not hasattr(self, 'tabla_encontrada') or not self.tabla_encontrada:
            QtWidgets.QMessageBox.warning(self, "Error", "Primero debe buscar un producto antes de actualizar.")
            return

        codigo = self.codigoeditar.text().strip()
        if not codigo:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, ingrese un código antes de actualizar.")
            return

        # Obtener los valores de los campos de entrada
        precio = self.precioeditar.text().strip()
        nombre = self.nombreeditar.text().strip()
        cantidad = self.candtidadeditar.text().strip()
        proveedor = self.proveedoreeditar.text().strip()

        campos = []
        valores = []

        if precio:
            try:
                precio = float(precio)
                campos.append("precio = %s")
                valores.append(precio)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Error", "Precio debe ser un número.")
                return

        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)

        if cantidad:
            try:
                cantidad = int(cantidad)
                campos.append("cantidad = %s")
                valores.append(cantidad)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Error", "Cantidad debe ser un entero.")
                return

        if proveedor:
            campos.append("proveedor = %s")
            valores.append(proveedor)

        if not campos:
            QtWidgets.QMessageBox.warning(self, "Error", "No hay campos para actualizar.")
            return

        # Ejecutar consulta SQL para actualizar solo los campos proporcionados
        set_clause = ", ".join(campos)
        query = f"UPDATE {self.tabla_encontrada} SET {set_clause} WHERE codigo = %s"
        valores.append(codigo)

        cursor = self.db.dbcursor
        try:
            cursor.execute(query, tuple(valores))
            if cursor.rowcount > 0:
                self.db.commit()
                QtWidgets.QMessageBox.information(self, "Éxito", "El producto se actualizó correctamente.")

                # Limpiar campos y tabla de edición
                self.codigoeditar.clear()
                self.precioeditar.clear()
                self.nombreeditar.clear()
                self.candtidadeditar.clear()
                self.proveedoreeditar.clear()
                self.tableeditar.setRowCount(0)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No se encontró ningún producto con ese código para actualizar.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error al actualizar el producto: {e}")


    def buscarcodeeliminar(self):
        codigo = self.codigoeliminar.text().strip()

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
        self.tableeliminar.setRowCount(1)
        self.tableeliminar.setColumnCount(6)
        for col_idx, value in enumerate(resultado):
            self.tableeliminar.setItem(0, col_idx, QtWidgets.QTableWidgetItem(str(value)))

    def eliminar_producto(self):
        # Verificar si se encontró una tabla y un producto
        if not self.tabla_encontrada:
            QtWidgets.QMessageBox.warning(self, "Error", "Primero debe buscar un producto antes de eliminarlo.")
            return

        # Obtener el código del producto
        codigo = self.codigoeliminar.text().strip()

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

                # Limpiar el tableWidget y el campo de texto
                self.tableeliminar.setRowCount(0)
                self.codigoeliminar.clear()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No se encontró ningún producto con ese código para eliminar.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error al eliminar el producto: {e}")

def a3(db, widget): 
    almacen_w = Almacen(widget, db)
    widget.addWidget(almacen_w)
    widget.setFixedWidth(1091)
    widget.setFixedHeight(501)
    widget.setCurrentIndex(widget.currentIndex() + 1)