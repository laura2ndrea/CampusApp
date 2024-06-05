import data.datos as dataOpciones
import menu.opciones as menuOpciones

def asignarCamper_ruta():
    campers = dataOpciones.cargar_datos("data/campers.json")
    rutas = dataOpciones.cargar_datos("data/rutas.json")
    
    doc_camper = input("Ingrese el documento del camper: ").strip()
    
    if doc_camper not in campers:
        print("El documento ingresado no corresponde a ningún camper.")
        return

    if campers[doc_camper]['estado'] != 'Aprobado':
        print("El camper debe tener en su estado aprobado, para ser asignado a una ruta.")
        return
    
    print("Rutas disponibles:")
    for idx, ruta in enumerate(rutas.keys(), 1):
        print(f"{idx}. {ruta}")
    
    while True:
        try:
            ruta_idx = int(input("Seleccione una ruta (número): ")) - 1
            if ruta_idx < 0 or ruta_idx >= len(rutas):
                raise IndexError("El número seleccionado no corresponde a ninguna ruta.")
            ruta_seleccionada = list(rutas.keys())[ruta_idx]
            break
        except ValueError:
            print("Debe ingresar un número válido.")
        except IndexError as ie:
            print(f"Error: {ie}")
    
    grupos_disponibles = {grupo: datos for grupo, datos in rutas[ruta_seleccionada]['grupos'].items() if datos['cantidad_campers'] < 33}
    
    if not grupos_disponibles:
        print(f"Todos los cursos de la {ruta_seleccionada} están llenos.")
        return
    
    print(f"Grupos disponibles en {ruta_seleccionada}:")
    for grupo, datos in grupos_disponibles.items():
        print(f"{grupo} - {datos['cantidad_campers']} inscritos")
    
    while True:
        grupo_seleccionado = input("Ingrese el grupo en el que desea inscribir al camper: ").strip().capitalize()
        if grupo_seleccionado in grupos_disponibles:
            break
        else:
            print("El grupo seleccionado no es válido. Ingrese nuevamente el grupo.")

    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['campers_ids'].append(doc_camper)
    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['cantidad_campers'] += 1
    campers[doc_camper]['estado'] = 'Cursando'
    
    dataOpciones.guardar_datos("data/rutas.json", rutas)
    dataOpciones.guardar_datos("data/campers.json", campers)
    
    print(f"El camper {doc_camper} ha sido asignado correctamente a {ruta_seleccionada}, grupo {grupo_seleccionado}.")

def asignarTrainer_ruta(): 
    trainers = dataOpciones.cargar_datos("data/trainers.json")
    rutas = dataOpciones.cargar_datos("data/rutas.json")

    trainers_disponibles = {tr_doc: tr_info for tr_doc, tr_info in trainers.items() if any(disponibilidad == "Disponible" for disponibilidad in tr_info['horario_disponible'].values())}

    if not trainers_disponibles:
        print("No hay trainers disponibles en este momento.")
        return
    
    trainers_list = list(trainers_disponibles.items())
    print("Trainers disponibles y horarios:")
    for docx, (trainer_doc, trainer_info) in enumerate(trainers_list, 1):
        print(f"{docx}. Documento: {trainer_doc}")
        print(f"   Nombre: {trainer_info['nombres']} {trainer_info['apellidos']}")
        menuOpciones.mini_separador()

    while True:
        try:
            trainer_docx = int(input("Seleccione un trainer (número): ")) 
            if 1 <= trainer_docx <= len(trainers_list):
                break
            else:
                print("Número de trainer fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    trainer_doc = trainers_list[trainer_docx - 1][0]
    trainer_info = trainers_list[trainer_docx - 1][1]

    horarios_disponibles = [horario for horario, disponibilidad in trainer_info['horario_disponible'].items() if disponibilidad == "Disponible"]
    print("Horarios disponibles para el trainer seleccionado:")
    for num, horario in enumerate(horarios_disponibles, 1):
        print(f"{num}. {horario}")

    while True:
        try:
            horario_id = int(input("Seleccione un horario (número): ")) 
            if 1 <= horario_id <= len(horarios_disponibles):
                break
            else:
                print("Número de horario fuera de rango.")
        except ValueError:
            print("Debe ingresar un número.")

    horario_seleccionado = horarios_disponibles[horario_id - 1]

    print("Rutas disponibles:")
    for num, ruta in enumerate(rutas.keys(), 1):
        print(f"{num}. {ruta}")

    while True:
        try:
            ruta_id = int(input("Seleccione una ruta (número): ")) 
            if ruta_id < 0 or ruta_id >= len(rutas):
                raise IndexError("El número seleccionado no corresponde a ninguna ruta.")
            break
        except (ValueError, IndexError):
            print("Selección no válida, intente nuevamente.")

    ruta_seleccionada = list(rutas.keys())[ruta_id - 1]
    grupos_disponibles = {grupo: info for grupo, info in rutas[ruta_seleccionada].get('grupos', {}).items() if info['trainer_id'] == ""}

    if not grupos_disponibles:
        print("No hay grupos disponibles en esta ruta.")
        return

    print("Grupos disponibles:")
    for grupo in grupos_disponibles:
        print(f"- {grupo}")

    while True:
        grupo_seleccionado = input("Ingrese el grupo en el que desea asignar al trainer: ").strip().capitalize()
        if grupo_seleccionado not in grupos_disponibles:
            print("El grupo seleccionado no es válido. Intente nuevamente.")
        else:
            break

    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['trainer_id'] = trainer_doc
    rutas[ruta_seleccionada]['grupos'][grupo_seleccionado]['horario'] = horario_seleccionado
    trainers[trainer_doc]['horario_disponible'][horario_seleccionado] = "No disponible"

    dataOpciones.guardar_datos('data/trainers.json', trainers)
    dataOpciones.guardar_datos('data/rutas.json', rutas)

    print(f"El trainer {trainer_info['nombres']} {trainer_info['apellidos']} asignado a la ruta {ruta_seleccionada}, grupo {grupo_seleccionado}, horario {horario_seleccionado}.")