from Classes.dbconn import DataB

db = DataB() #Crea la instancia de la DB
if db.connect():
    from Ui.a_login import a1
    a1(db)