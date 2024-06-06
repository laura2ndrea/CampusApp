opc_principal = ("1. Coordinación", "2. Trainers", "3. Campers", "4. Salir del programa")

opc_coordinacion = ("1. Gestión de matrículas", "2. Gestión de reportes", "3. Gestión de rutas", "4. Gestión de campers", "5. Salir del menú")

opc_gestionMatricula = ("1. Asignación de campers a rutas", "2. Asignacion de trainers a rutas", "3. Asignacion de fechas a rutas", "4. Asignación de salones a rutas", "5. Salir del menú")

opc_gestionReportes = ("1. Mostrar campers inscritos", "2. Mostrar campers aprobados", "3. Mostrar lista de trainers", "4. Mostrar campers de bajo rendimiento", "5. Mostrar trainers y campers asociados a rutas de entrenamiento", "6. Mostrar cantidad de campers aprobados y no aprobados por módulo", "7. Salir del menú")

opc_gestionRutas = ("1. Mostrar rutas de entrenamiento", "2. Crear nueva ruta de entrenamiento", "3. Crear nuevo grupo", "4. Salir del menú")

opc_gestionCampers = ("1. Inscripción de nuevo camper", "2. Actualizar información de campers", "3. Cambiar estado de camper", "4. Ingresar notas de prueba de ingreso", "5. Crear advertencias para campers", "6. Salir del menú")

opc_trainers = ("1. Mostrar información personal", "2. Mostrar rutas asignadas", "3. Ingresar notas", "4. Salir del menú")

opc_campers = ("1. Mostrar información personal", "2. Mostrar información de ruta asignada", "3. Mostrar notas", "4. Salir del menú")

def recorrer_opciones(opciones): 
    for i in opciones:
        print(i)
    separador()
    opcion = input("Ingrese la opción deseada: ")
    return opcion

def separador(): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def mini_separador(): 
    print("**************************")