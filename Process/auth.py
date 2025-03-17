def auth(db):
    from Classes.users import usuario, recepcion, caja, bodega, cocina
    from Ui.login_ui import a1
    
    # Obtiene los datos de inicio de sesión
    id_emp, pwd_emp = a1()
    
    if id_emp and pwd_emp:
        usr = usuario(id_emp,pwd_emp)
        # Pasa los datos de inicio de sesión al método login
        rol = usr.login(db)
        
        if rol == "Recepcion":
            role = recepcion()
            role.function()
        elif rol == "Caja":
            role = caja()
            role.function()
        elif rol == "Bodega":
            role = bodega()
            role.function()
        elif rol == "Cocina":
            role = cocina()
            role.function()
        else:
            print("Id o Password incorrectos")
    else:
        print("Inicio de sesion cancelado")