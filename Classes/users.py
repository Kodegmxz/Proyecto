class usuario:
    def __init__(self,id_emp,password):
        self._id_emp = id_emp
        self._password = password

    def login(self,db,widget):
        db.dbcursor.execute("SELECT rol FROM Users.rol WHERE id_emp = %s AND password = %s", (self._id_emp, self._password)) #Usando el argumento para usar el cursor
        result = db.dbcursor.fetchone()

        if result[0] == "Recepcion":
            from Ui.Recepcion.a_recep import a2
            a2(db,widget)