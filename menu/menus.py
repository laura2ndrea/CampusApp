import menu.opciones as menuOpciones
import data.datos as dataOpciones
import gestion.matriculas as matriculasOpciones
import gestion.campers as campersOpciones
import gestion.trainers as trainersOpciones
import gestion.rutas as rutasOpciones

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
    if not ingreso_coordinador():
        return
    while True: 
        menuOpciones.separador()
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

def menu_trainer():
    primer_ingreso = True
    doc_trainer = None

    if primer_ingreso or ingreso_exitoso:
            ingreso_exitoso, doc_trainer = ingreso_trainer()
            primer_ingreso = False

    while True:
        menuOpciones.separador()
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_trainers)
        if opcion == "1": 
            trainersOpciones.mostrarInformacion_trainer(doc_trainer)
        elif opcion == "2": 
            trainersOpciones.verRutas_trainers(doc_trainer)
        elif opcion == "3": 
            trainersOpciones.ingresarNotas_camper(doc_trainer)
        elif opcion == "4": 
            print("Saliendo ...")
            break
        else: 
            print ("Valor invalido, por favor ingrese una opcion nuevamente")

def menu_camper():
    doc = input("Ingrese su documento: ").strip() 
    if ingreso_camper(doc):
        while True: 
            menuOpciones.separador()
            print("Bienvenido camper, por favor seleccione una opción: ")
            opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_campers)
            if opcion == "1": 
                campersOpciones.monstrarInformacion_camper(doc)
            elif opcion == "2": 
                campersOpciones.mostrarRuta_camper(doc)
            elif opcion == "3": 
                campersOpciones.mostrarNotas_camper(doc)
            elif opcion == "4": 
                print("Saliendo ...")
                break
            else: 
                print ("Valor invalido, por favor ingrese una opcion nuevamente")
    else: 
        print("Ese documento no se encuentra registrado")

def menu_gestionMatricula(): 
    while True: 
        menuOpciones.separador()
        print("Por favor seleccione una opción: ")
        opcion = menuOpciones.recorrer_opciones(menuOpciones.opc_gestionMatricula)
        if opcion == "1": 
           matriculasOpciones.asignarCamper_ruta()
        elif opcion == "2": 
            matriculasOpciones.asignarTrainer_ruta()
        elif opcion == "3": 
            matriculasOpciones.asignarFechas_ruta()
        elif opcion == "4": 
            matriculasOpciones.asignarSalon_ruta()
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
            campersOpciones.mostrar_campers("Inscrito")
        elif opcion == "2": 
            campersOpciones.mostrar_campers("Aprobado")
        elif opcion == "3": 
            trainersOpciones.mostrar_trainers()
        elif opcion == "4": 
            campersOpciones.campers_bajoRendimiento()
        elif opcion == "5": 
            rutasOpciones.trainers_campers_grupo()
        elif opcion == "6": 
            rutasOpciones.notas_modulos()
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
           rutasOpciones.mostrar_rutas()
        elif opcion == "2": 
            rutasOpciones.crear_ruta()
        elif opcion == "3": 
            rutasOpciones.crear_grupo()
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
           campersOpciones.crear_camper()
        elif opcion == "2": 
            campersOpciones.actualizar_camper()
        elif opcion == "3": 
            campersOpciones.cambiar_estado()
        elif opcion == "4": 
            campersOpciones.notas_prueba_ingreso()
        elif opcion == "5":
            campersOpciones.crear_advertencias()
        elif opcion == "6": 
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
        return True, doc
    else:
        print("Contraseña o documento incorrecto")
        return False, None
    
def ingreso_camper(doc): 
    campers = dataOpciones.cargar_datos("data/campers.json")
    if doc in campers:
        return True
    else:
        return False