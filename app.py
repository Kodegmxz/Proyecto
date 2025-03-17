from Classes.dbconn import DataB

db = DataB() #Crea la instancia de la DB
if db.connect():
    from Process.auth import auth
    auth(db)  # Llama a la funcion auth con la instancia de la DB