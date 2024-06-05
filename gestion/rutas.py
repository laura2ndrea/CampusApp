import data.datos as dataOpciones
import menu.opciones as menuOpciones

def trainers_campers_grupo(): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    trainers = dataOpciones.cargar_datos("data/trainers.json")
    campers = dataOpciones.cargar_datos("data/campers.json")

    if not rutas:
        print("No hay rutas disponibles.")
        return

    print("Rutas disponibles:")
    rutas_list = list(rutas.keys())
    for idx, ruta in enumerate(rutas_list, 1):
        print(f"{idx}. {ruta}")

    while True:
        try:
            ruta_idx = int(input("Seleccione una ruta (número): "))
            if 1 <= ruta_idx <= len(rutas_list):
                break
            else:
                print("Número de ruta fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    ruta_seleccionada = rutas_list[ruta_idx - 1]
    grupos_disponibles = rutas[ruta_seleccionada].get('grupos', {})

    grupos_con_trainers = {grupo: info for grupo, info in grupos_disponibles.items() if info.get('trainer_id')}
    
    if not grupos_con_trainers:
        print("No hay grupos con trainers asignados en esta ruta.")
        return

    print("Grupos disponibles:")
    grupos_list = list(grupos_con_trainers.keys())
    for idx, grupo in enumerate(grupos_list, 1):
        print(f"{idx}. {grupo}")

    while True:
        try:
            grupo_idx = int(input("Seleccione un grupo (número): "))
            if 1 <= grupo_idx <= len(grupos_list):
                break
            else:
                print("Número de grupo fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    grupo_seleccionado = grupos_list[grupo_idx - 1]
    info_grupo = grupos_con_trainers[grupo_seleccionado]
    trainer_id = info_grupo['trainer_id']
    
    trainer_nombre = f"{trainers[trainer_id]['nombres']} {trainers[trainer_id]['apellidos']}"

    campers_asociados = info_grupo.get('campers_ids', [])

    print(f"Trainer asignado al grupo {grupo_seleccionado}: {trainer_nombre}")

    print("Campers inscritos:")
    for camper_id in campers_asociados:
        if camper_id in campers:
            camper_nombre = f"{campers[camper_id]['nombres']} {campers[camper_id]['apellidos']}"
            print(f"- {camper_nombre}")
        else:
            print(f"- Camper con documento {camper_id} no encontrado")

def notas_modulos(): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    notas = dataOpciones.cargar_datos("data/notas.json")

    if not rutas:
        print("No hay rutas disponibles.")
        return

    print("Rutas disponibles:")
    rutas_list = list(rutas.keys())
    for idx, ruta in enumerate(rutas_list, 1):
        print(f"{idx}. {ruta}")

    while True:
        try:
            ruta_idx = int(input("Seleccione una ruta (número): "))
            if 1 <= ruta_idx <= len(rutas_list):
                break
            else:
                print("Número de ruta fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    ruta_seleccionada = rutas_list[ruta_idx - 1]
    grupos_disponibles = rutas[ruta_seleccionada].get('grupos', {})

    if not grupos_disponibles:
        print("No hay grupos disponibles en esta ruta.")
        return

    print("Grupos disponibles:")
    grupos_list = list(grupos_disponibles.keys())
    for idx, grupo in enumerate(grupos_list, 1):
        print(f"{idx}. {grupo}")

    while True:
        try:
            grupo_idx = int(input("Seleccione un grupo (número): "))
            if 1 <= grupo_idx <= len(grupos_list):
                break
            else:
                print("Número de grupo fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    grupo_seleccionado = grupos_list[grupo_idx - 1]
    info_grupo = grupos_disponibles[grupo_seleccionado]
    campers_asociados = info_grupo.get('campers_ids', [])

    if not campers_asociados:
        print("No hay campers inscritos en este grupo.")
        return

    modulos_disponibles = list(notas[list(campers_asociados)[0]]['modulos'].keys())
    if not modulos_disponibles:
        print("No hay módulos disponibles para los campers en este grupo.")
        return

    print("Módulos disponibles:")
    for idx, modulo in enumerate(modulos_disponibles, 1):
        print(f"{idx}. {modulo}")

    while True:
        try:
            modulo_idx = int(input("Seleccione un módulo (número): "))
            if 1 <= modulo_idx <= len(modulos_disponibles):
                break
            else:
                print("Número de módulo fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    modulo_seleccionado = modulos_disponibles[modulo_idx - 1]

    aprobados = 0
    no_aprobados = 0

    for camper_id in campers_asociados:
        camper_notas = notas.get(camper_id)
        if camper_notas:
            modulos_camper = camper_notas.get('modulos', {})
            estado = modulos_camper.get(modulo_seleccionado, {}).get('estado')
            if estado == "Aprobado":
                aprobados += 1
            else:
                no_aprobados += 1

    print(f"Módulo seleccionado: {modulo_seleccionado}")
    print(f"Cantidad de campers aprobados: {aprobados}")
    print(f"Cantidad de campers no aprobados: {no_aprobados}")

def mostrar_rutas(): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    
    print("Rutas de entrenamiento y sus grupos:")
   
    for ruta_nombre, ruta_info in rutas.items():
        print(f"Nombre de la ruta: {ruta_nombre}")
        print("Grupos disponibles:")
        for grupo in ruta_info['grupos'].keys():
            print(f" - {grupo}")
        menuOpciones.mini_separador()

def crear_ruta(): 
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    
    nueva_ruta = {}
    
    while True:
        nombre_ruta = input("Ingrese el nombre de la nueva ruta: ").strip()
        if nombre_ruta in rutas:
            print("Esa ruta ya existe. Ingrese un nombre diferente.")
        else:
            break
    
    modulos_predefinidos = [
        "Fundamentos de programación",
        "Programación Web",
        "Programación formal",
        "Bases de datos",
        "Backend"
    ]
    
    modulos = {}
    
    for modulo in modulos_predefinidos:
        print(f"Ingrese los temas para el módulo '{modulo}':")
        temas = []
        if modulo == "Bases de datos":
            temas = []
            for i in range(2):  
                temas.append(input(f"Ingrese el tema {i+1} para 'Bases de datos': ").strip())
            modulos[modulo] = {
                "sgdb_principal": temas[0],
                "sgdb_alternativo": temas[1]
            }
        else: 
            while True:
                tema = input("Ingrese el nombre del tema (o 'q' para terminar con este módulo): ").strip()
                if tema.lower() == 'q':
                    break
                temas.append(tema)
                modulos[modulo] = temas
        
    
    nueva_ruta["modulos"] = modulos
    nueva_ruta["grupos"] = {}  
    
    rutas[nombre_ruta] = nueva_ruta
    
    dataOpciones.guardar_datos("data/rutas.json", rutas)
    print(f"La nueva ruta '{nombre_ruta}' ha sido creada exitosamente.")

def crear_grupo(): 

    rutas = dataOpciones.cargar_datos("data/rutas.json")
    
    print("Rutas disponibles:")
    for ruta in rutas:
        print("-", ruta)

    while True:
        ruta_seleccionada = input("Ingrese el nombre de la ruta para crear el grupo: ").strip()
        if ruta_seleccionada not in rutas:
            print("La ruta especificada no existe. Por favor, ingrese una ruta válida.")
        else:
            break

    while True:
        nombre_grupo = input("Ingrese el nombre del nuevo grupo: ").strip().upper()
        if nombre_grupo in rutas[ruta_seleccionada]["grupos"]:
            print("El nombre del grupo ya existe en la ruta. Por favor, elija otro nombre.")
        else:
            break

    nuevo_grupo = {
        "trainer_id": "",
        "campers_ids": [],
        "fecha_inicio": "",
        "fecha_fin": "",
        "salon_entrenamiento": "",
        "horario": "",
        "cantidad_campers": 0
    }

    rutas[ruta_seleccionada]["grupos"][nombre_grupo] = nuevo_grupo

    dataOpciones.guardar_datos("data/rutas.json", rutas)

    print(f"Grupo '{nombre_grupo}' creado exitosamente en la ruta '{ruta_seleccionada}'.")