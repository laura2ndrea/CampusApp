import data.datos as dataOpciones

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