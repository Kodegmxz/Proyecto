
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from Ui.Almacen.a_agregar import AgregarProducto
from Ui.Almacen.a_editar import Editar
from Ui.Almacen.a_eliminar import Eliminar  # Importar el diálogo de eliminación

class Almacen(QtWidgets.QWidget):
    def __init__(self, widget, db):
        super(Almacen, self).__init__()
        self.widget = widget  # Guardar referencia al widget
        self.db = db  # Guardar referencia a la base de datos
        dir_a = os.path.dirname(os.path.abspath(__file__))
        ui_a = os.path.join(dir_a, "u_almacen.ui")
        loadUi(ui_a, self)

        # Conectar botones a sus funciones
        self.botonbuscar.clicked.connect(self.buscar_producto)
        self.botonreset.clicked.connect(self.resetear_tabla)
        self.agregar_2.clicked.connect(self.abrir_agregar_producto)
        self.editar.clicked.connect(self.abrir_editar_producto)
        self.eliminar.clicked.connect(self.abrir_eliminar_producto) 

        self.cargar_datos_iniciales()

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

    def abrir_agregar_producto(self):
        # Crear una instancia del diálogo AgregarProducto
        agregar_producto_dialog = AgregarProducto(self.db)
        
        # Conectar la señal producto_agregado al método cargar_datos_iniciales
        agregar_producto_dialog.producto_agregado.connect(self.cargar_datos_iniciales)
        
        # Mostrar el diálogo
        agregar_producto_dialog.exec_()
        
    def abrir_editar_producto(self):
        # Crear una instancia del diálogo Editar
        editar_producto_dialog = Editar(self.db)
        
        # Conectar la señal actualizarTablaSignal al método cargar_datos_iniciales
        editar_producto_dialog.actualizarTablaSignal.connect(self.cargar_datos_iniciales)
        
        # Mostrar el diálogo
        editar_producto_dialog.exec_()

    def abrir_eliminar_producto(self):
        # Crear una instancia del diálogo Eliminar
        eliminar_producto_dialog = Eliminar(self.db)
        
        # Conectar la señal actualizarTablaSignal al método cargar_datos_iniciales
        eliminar_producto_dialog.actualizarTablaSignal.connect(self.cargar_datos_iniciales)
        
        # Mostrar el diálogo
        eliminar_producto_dialog.exec_()


def a3(db, widget): 
    almacen_w = Almacen(widget, db)
    widget.addWidget(almacen_w)
    widget.setFixedWidth(931)
    widget.setFixedHeight(641)
    widget.setCurrentIndex(widget.currentIndex() + 1)