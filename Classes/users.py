
class usuario:
    def __init__(self,id_emp,password):
        self._id_emp = id_emp
        self._password = password
    def login(self,db):
        db.dbcursor.execute("SELECT rol FROM Users.rol WHERE id_emp = %s AND password = %s", (self._id_emp, self._password)) #Usando el argumento para usar el cursor
        result = db.dbcursor.fetchone()
        if result:
            return result[0]

    def function(self):
        pass

class recepcion(usuario):
    def __init__(self):
        pass

    def function(self):
        pass


class caja(usuario):
    def __init__(self):
        pass

    def function(self):
        pass

class bodega(usuario):
    def __init__(self):
        pass

    def function(self):
        pass

class cocina(usuario):
    def __init__(self):
        pass

    def function(self):
        pass