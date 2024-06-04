import menu.opciones as menuOpciones
import data.datos as dataOpciones

def menu_principal():
     while True: 
        menuOpciones.separador()
        print("Bienvenido al menú principal, por favor indique su rol: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_principal)
        if opcion == "1": 
           menu_coordinador()
        elif opcion == "2": 
            menu_trainer()
        elif opcion == "3": 
            menu_camper()
        elif opcion == "4": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_coordinador(): 
    while True: 
        menuOpciones.separador()
        ingreso = ingreso_coordinador()
        if ingreso == True: 
            print("Bienvenido coordinador, por favor seleccione una opción: ")
            opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_coordinacion)
            if opcion == "1": 
                menu_gestionMatricula()
            elif opcion == "2": 
                menu_gestionReportes()
            elif opcion == "3": 
                menu_gestionRutas()
            elif opcion == "4": 
                menu_gestionCampers()
            elif opcion == "5": 
                print("Saliendo ...")
                break
            else: 
                print ("Valor invalido, por favor ingrese una opcion nuevamente")
        else: 
            break

def menu_trainer(): 
    while True: 
        menuOpciones.separador()
        ingreso = ingreso_trainer()
        if ingreso == True: 
            opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_trainers)
            if opcion == "1": 
                print("En construccion")
            elif opcion == "2": 
                print("trainers")
            elif opcion == "3": 
                print ("campers")
            elif opcion == "4": 
                print("Saliendo ...")
                break
            else: 
                print ("Valor invalido, por favor ingrese una opcion nuevamente")
        else: 
            break

def menu_camper(): 
    while True: 
        menuOpciones.separador()
        print("Bienvenido camper, por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_campers)
        if opcion == "1": 
           print("En construccion")
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print ("En construcción ...")
        elif opcion == "5": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_gestionMatricula(): 
    while True: 
        menuOpciones.separador()
        print("Por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_gestionMatricula)
        if opcion == "1": 
           print("En construccion")
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print ("En construcción ...")
        elif opcion == "5": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_gestionReportes(): 
    while True: 
        menuOpciones.separador()
        print("Por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_gestionReportes)
        if opcion == "1": 
           print("En construccion")
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print ("En construcción ...")
        elif opcion == "5": 
            print ("En construcción ...")
        elif opcion == "6": 
            print ("En construcción ...")
        elif opcion == "7": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_gestionRutas(): 
    while True: 
        menuOpciones.separador()
        print("Por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_gestionRutas)
        if opcion == "1": 
           print("En construccion")
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_gestionCampers(): 
    while True: 
        menuOpciones.separador()
        print("Por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_gestionCampers)
        if opcion == "1": 
           print("En construccion")
        elif opcion == "2": 
            print("trainers")
        elif opcion == "3": 
            print ("campers")
        elif opcion == "4": 
            print ("En construcción ...")
        elif opcion == "5": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")


def ingreso_coordinador(): 
    pass_correcta = "passcord"
    password = input("Ingrese la contraseña del coordinador: ").strip()

    if password == pass_correcta: 
        print ("Contraseña correcta")
        return True
    else:
        print("Contraseña incorrecta")
        return False
    
def ingreso_trainer(): 
    trainers = dataOpciones.cargar_datos("data/trainers.json")
    doc = input("Ingrese su documento: ").strip()
    password = input("Ingrese su contraseña: ").strip()

    if doc in trainers and password == trainers[doc]["password"]:
        print(f"Contraseña correcta.\n Bienvenido, {trainers[doc]['nombres']} {trainers[doc]['apellidos']}.")
        return True
    else:
        print("Contraseña o documento incorrecto")
        return False